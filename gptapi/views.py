from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GPTRequestSerializer
from g4f.client import Client
import markdown
from markdownify import markdownify as md


class GPTResponseView(APIView):
    PROMPT_PREFIX = (
        ""
    )

    def post(self, request, *args, **kwargs):
        serializer = GPTRequestSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            modified_prompt = f"{self.PROMPT_PREFIX}{prompt}"

            client = Client()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": modified_prompt}],
            )

            # content = response.choices[0].message.content 응답 원문

            # 응답에서 마크다운 형식을 제거
            content = response.choices[0].message.content
            plain_text = md(content)

            return Response({'response': plain_text}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
