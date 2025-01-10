#!/usr/bin/env python3
import argparse
import os
import glob
import logging
import time
from pathlib import Path
from docling.document_converter import DocumentConverter
from docling_core.types.doc import ImageRefMode
from docling.datamodel.base_models import FigureElement, InputFormat, Table
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
IMAGE_RESOLUTION_SCALE = 2.0
_log = logging.getLogger(__name__)

def process_file(input_path: str, output_folder: str, with_images: bool) -> None:
    start_time = time.time()
    output_dir = Path(output_folder)

    # Important: For operating with page images, we must keep them, otherwise the DocumentConverter
    # will destroy them for cleaning up memory.
    # This is done by setting PdfPipelineOptions.images_scale, which also defines the scale of images.
    # scale=1 correspond of a standard 72 DPI image
    # The PdfPipelineOptions.generate_* are the selectors for the document elements which will be enriched
    # with the image field
    pipeline_options = PdfPipelineOptions()
    pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
    pipeline_options.generate_page_images = True
    pipeline_options.generate_picture_images = True
    
    """
    Processa um único arquivo usando a biblioteca docling e salva o resultado em um .md.
    """

     # Gera o nome de arquivo de saída
    # Exemplo: se input_path for "arquivo.pdf", o output será "arquivo.pdf.md"
    base_name = os.path.basename(input_path)  # "arquivo.pdf"
    output_name = base_name + ".md"           # "arquivo.pdf.md"

    

    # Instancia o conversor de documentos
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    # Converte o arquivo
    conv_res = converter.convert(input_path)

    # Save markdown with embedded pictures
    doc_filename = conv_res.input.file.stem
    
    # Save markdown with embedded pictures
    md_filename = output_dir / f"{doc_filename}-with-images.md"
    conv_res.document.save_as_markdown(md_filename, image_mode=ImageRefMode.EMBEDDED)

    end_time = time.time() - start_time

    _log.info(f"Document converted and figures exported in {end_time:.2f} seconds.")

    """ # Extrai o texto em formato Markdown
    markdown_text = result.document.export_to_markdown()
    print(f"Arquivo markdown sem imagens em: {output_folder + output_name}")
   
    # Garante que a pasta de saída exista
    os.makedirs(output_folder, exist_ok=True)

    # Monta o caminho completo do arquivo de saída
    output_path = os.path.join(output_folder, output_name)

    # Salva o texto Markdown no arquivo de saída
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)
    

    # Com Imagens
    # Save markdown with embedded pictures
    doc_filename = result.input.file.stem
    print(f"doc_filename: {doc_filename}")

    # Save markdown with externally referenced pictures
    md_filename = f"{doc_filename}-with-image-refs.md"
    print(f"md_filename: {md_filename}")

    result.document.save_as_markdown(md_filename, image_mode=ImageRefMode.REFERENCED)
    """

    


def main():
    """
    Script principal para processar um ou vários arquivos usando docling.
    Pode receber:
      - --input_folder="pasta/arquivos/*" para processar múltiplos arquivos
      - --input_file="arquivo.pdf" para processar um único arquivo
      - --output_folder (opcional), se não informado, será usado 'output/'
    """
    parser = argparse.ArgumentParser(description="File2TextAI: Extrai texto de arquivos e converte para Markdown.")
    parser.add_argument("--input_folder", type=str, help="Caminho com glob para múltiplos arquivos. Exemplo: 'pasta/arquivos/*'")
    parser.add_argument("--input_file", type=str, help="Caminho para um único arquivo. Exemplo: 'arquivo.pdf'")
    parser.add_argument("--output_folder", type=str, default="output", 
                        help="Pasta onde serão salvos os arquivos de saída. Padrão: 'output'")

    args = parser.parse_args()

    # Verifica se será usado input_folder ou input_file
    if args.input_folder:
        # Processa todos os arquivos que correspondem ao padrão fornecido (incluindo subpastas)
        for file_path in glob.glob(args.input_folder, recursive=True):
            # Ignora se for diretório
            if not os.path.isdir(file_path):
                process_file(file_path, args.output_folder, with_images=True)
    elif args.input_file:
        # Processa apenas um arquivo
        if os.path.isfile(args.input_file):
            process_file(args.input_file, args.output_folder, with_images=True)
        else:
            print(f"Arquivo não encontrado: {args.input_file}")
    else:
        print("Nenhum parâmetro de entrada fornecido. Use --input_folder ou --input_file.")


if __name__ == "__main__":
    main()
# python3 main.py --input_file=pdfs/artigo-docling.pdf --output_folder=output/