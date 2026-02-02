# DevOps Assessment

Este proyecto implementa un microservicio bajo estándares de DevOps, incluyendo:
- **API**: FastAPI con validación de headers y modelos Pydantic.
- **Pruebas**: Suite de tests con Pytest.
- **Contenerización**: Dockerfile optimizado.
- **Infraestructura**: Código Terraform para despliegue con Load Balancer.
- **CI/CD**: Pipeline automático en GitHub Actions.

## Cómo probar localmente:
1. `pip install -r requirements.txt`
2. `uvicorn main:app --reload`
3. Acceder a `http://127.0.0.1:8000/docs` para probar el endpoint POST /DevOps.