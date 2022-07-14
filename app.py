# para usar o modificador de imagens, instale o pillow
# pip install pillow
import os
from PIL import Image


def main(main_images_folder, new_width=800):
    if not os.path.isdir(main_images_folder):
        raise NotADirectoryError(f'{main_images_folder} não existe.')  # teste rápido de erro

    for root, dirs, files in os.walk(main_images_folder):
        for file in files:
            print('Definindo caminho dos arquivos e separando extensões')
            file_full_path = os.path.join(root, file)
            file_name, extension = os.path.splitext(file)
            if extension == '.jpg' or extension == '.png' or extension == '.jpeg':  # pegando apenas imagens
                print('Separando apenas as fotos das pastas')
                converted_tag = '_CONVERTED'  # para não ocorrer sobreposição
                new_file = file_name + converted_tag + extension  # para não sobrescrever o original
                new_file_full_path = os.path.join(root, new_file)

                # caso queira apagar as imagens convertidas
                # if converted_tag in file_full_path:
                #     os.remove(file_full_path)
                # continue

                if os.path.isfile(new_file_full_path):  # confirmando a existência do arquivo
                    print(f'Arquivo {new_file_full_path} já existe!')  # todo implementar função de escolher sim ou não
                    continue

                if converted_tag in file_full_path:  # com isso caso já tenho o converted tag na imagem ele não converte novamente
                    print('Arquivo já convertido')
                    continue

                img_pillow = Image.open(file_full_path)
                # exif = img_pillow._getexif()
                # print(exif.get(36867))  # é a TAG da data que está nos metadadados da imagem

                width, height = img_pillow.size  # pegando largura e altura da imagem

                # conta para descobrir a altura baseada na largura pré-definida
                new_height = round(new_width * height / width)  # regra de 3 -- round arredonda para inteiro
                '''
                width       height
                new_width   ??
                '''

                # criando a nova imagem
                new_image = img_pillow.resize((new_width, new_height),
                                              Image.Resampling.LANCZOS)  # LANCZOS é um calculo matemático para resize da imagem

                # salvando a imagem
                new_image.save(new_file_full_path,
                               optmize=True,
                               quality=100)  # exif=img_pillow.info['exif'])  # exif usado para manter os metadados da img

                print(f'{file_full_path} convertido com sucesso!')
                new_image.close()
                img_pillow.close()  # para garantir que vai encerrar o processo no final

                # caso queria excluir as imagens originais
                # os.remove(file_full_path)


if __name__ == '__main__':
    print('***REDIMENSÃO DE FOTOS***')
    print('*OBS: Todas as subpastas do caminho determinado também serão convertidas!*')
    main_images_folder = input('Caminho das fotos: ')  # definindo a pasta raiz de onde vai pegar as imagens
    print('*OBS: Altura da imagem é calculada de acordo com sua largura!*')
    largura = int(input('Defina a Largura da Imagem: '))
    main(main_images_folder, new_width=largura)
