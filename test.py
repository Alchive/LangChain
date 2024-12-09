from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM


# Ollama 모델 초기화
llm = OllamaLLM(model="llama3.1:latest")

# 템플릿 정의
template = "{country}의 수도는?"
prompt = PromptTemplate.from_template(template=template)

# 체인 생성: PromptTemplate -> LLM -> OutputParser
chain = prompt | llm | StrOutputParser()

# 데이터 입력 (딕셔너리 형태로 키-값 쌍 제공)
result = chain.invoke(input={"country": "한국"})

# 결과 출력
print(result)
