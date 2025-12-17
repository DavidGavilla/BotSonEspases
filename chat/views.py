from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import os

from rag_api.BotLogic.Controlador import Controlador

controlador = Controlador(
    api_key=os.getenv("GEMINI_API_KEY"),
    token=os.getenv("TELEGRAM_BOT_TOKEN"),
    start_bot=False,
)

@api_view(['POST'])
def hacer_pregunta(request):
    user_id = request.data.get('user_id')
    message = request.data.get('message')

    if not user_id or not message:
        return Response({"error": "Faltan parámetros 'user_id' o 'message'."},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        respuesta = controlador.hacer_pregunta(message, int(user_id)) 
        return Response({"response": respuesta}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def clear(request):
    try:
        controlador.limpiar_todo()
        return Response({"ok": True})
    except Exception as e:
        return Response({"error": "internal_error", "detail": str(e)},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
