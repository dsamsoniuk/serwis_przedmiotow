import logging

# Example usage:
#
# lm = loggerModule()
# logger = lm.getLogger()
# logger.debug("To jest log DEBUG (najbardziej szczegółowy)")
# logger.debug("To jest log DEBUG (najbardziej szczegółowy)")
# logger.info("To jest log INFO (informacja)")
# logger.warning("To jest log WARNING (ostrzeżenie)")
# logger.error("To jest log ERROR (błąd)")
# logger.critical("To jest log CRITICAL (poważny błąd)")

class loggerModule:
    def __init__(self):
        
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler("app.log"),    
                logging.StreamHandler()            
            ]
        )
        self.logger = logging.getLogger("my_app")
    def getLogger(self):
        return self.logger