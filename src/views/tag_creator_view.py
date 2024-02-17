from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controllers import TagCreateTagController


class TagCreatorView:
    """
    Responsability for interating with http
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = TagCreateTagController()

        body = http_request.body
        product_code = body["product_code"]

        # logica de regra de negócio - criação das tags
        formatted_response = tag_creator_controller.create(product_code)
        # retorno http
        return HttpResponse(status_code=200, body=formatted_response)
