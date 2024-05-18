import argparse
import os


from src.file_creator.generators import exe_generator, java_generator
from src.file_cracker.crackers import dotnet_cracker, general_cracker
from src.file_creator.utils.logger import setup_logger


def main():
    # Ustawienia loggera
    logger = setup_logger('main_logger', 'app.log')
    logger.info('Application started')

    # Parser argumentów
    parser = argparse.ArgumentParser(description="EducationalApp-CRACKER")
    parser.add_argument('--mode', type=str, required=True,
                        choices=['generate_exe', 'generate_jar', 'crack_dotnet', 'crack_general'],
                        help='Tryb pracy aplikacji')
    parser.add_argument('--input', type=str, required=True, help='Ścieżka do pliku wejściowego')
    parser.add_argument('--output', type=str, help='Ścieżka do pliku wyjściowego')

    args = parser.parse_args()

    # Wybór trybu pracy
    if args.mode == 'generate_exe':
        if not args.output:
            parser.error("generate_exe mode requires --output argument")
        exe_generator.generate_exe(args.input, args.output)
        logger.info(f'Generated exe file from {args.input} to {args.output}')
    elif args.mode == 'generate_jar':
        if not args.output:
            parser.error("generate_jar mode requires --output argument")
        java_generator.generate_java_jar(args.input, args.output)
        logger.info(f'Generated jar file from {args.input} to {args.output}')
    elif args.mode == 'crack_dotnet':
        dotnet_cracker.crack_dotnet_exe(args.input)
        logger.info(f'Cracked .NET exe file at {args.input}')
    elif args.mode == 'crack_general':
        general_cracker.crack_general_exe(args.input)
        logger.info(f'Cracked general exe file at {args.input}')
    else:
        parser.error("Invalid mode")

    logger.info('Application finished')


if __name__ == "__main__":
    main()
