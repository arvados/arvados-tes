import connexion
from connexion.resolver import RelativeResolver

def main():
    app = connexion.FlaskApp(__name__, port = 8080, specification_dir='openapi/', server='tornado')

    app.add_api('task_execution_service.openapi.yaml', resolver=RelativeResolver('arvados_tes.handlers'))

    app.run(port=5000, debug=True)
