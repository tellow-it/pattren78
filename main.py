from logger import Logger

if __name__ == "__main__":
    logger = Logger(path_log=r'C:\Users\mrtik\PycharmProjects\PatternsLab')
    logger1 = Logger(path_log=r'C:\Users\mrtik\PycharmProjects\PatternsLab\test')
    logger.write_log(message='All works', status='INFO')
    logger1.write_log(message='All works1', status='INFO')

