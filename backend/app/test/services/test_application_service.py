import importlib 
import inspect 
import pytest 


class TestApplicationServiceStructure:
    def test_if_is_running(self) -> None:
        assert True 
        
    def test_if_can_import_the_service_class(self) -> None:
        try:
            from app.services.application_service import ApplicationService 
            assert inspect.isclass(ApplicationService)
            assert ApplicationService is not None
        except ImportError:
            raise ImportError("Was not possible to import the application service class and file ")
        
    def test_if_application_service_have_correct_methods(self) -> None:
        module = importlib.import_module("app.services.application_service")
        class_ = module.ApplicationService
        assert hasattr(class_, "create_application"), "O servico nao possui o metodo create_application"
        assert hasattr(class_, "delete_application"), "O servico nao possui o metodo delete_application"
        assert hasattr(class_, "update_application"), "O servico nao possui o metodo update_application"
        assert hasattr(class_, "search_application_by_id"), "O servico nao possui o metodo search_application_by_id"
        assert hasattr(class_, "search_application"), "O servico nao possui o metodo search_application"
    
    def test_if_create_application_method_have_correct_parameters(self) -> None:
        module = importlib.import_module("app.services.application_service")
        class_ = module.ApplicationService
        # TODO: Verificar se assinatura possui parametros corretos
        
class TestApplicationServiceFunctions:
    def test_if_is_running(self) -> None:
        assert True
        
    def test_if_can_import_application_service(self) -> None:
        try:
            from app.services.application_service import ApplicationService 
            assert ApplicationService is not None 
            assert inspect.isclass(ApplicationService)
        except ImportError:
            raise ImportError("Nao foi possivel importar o servico de aplicacao de vagas")