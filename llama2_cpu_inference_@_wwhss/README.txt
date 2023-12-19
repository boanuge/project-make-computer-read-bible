================================================================================
Download for better results from https://huggingface.co/TheBloke/orca_mini_v2_13b-GGML
================================================================================

PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com\models> python
>>> from huggingface_hub import hf_hub_download
>>> hf_hub_download(repo_id="TheBloke/orca_mini_v2_13b-GGML", filename="orca_mini_v2_13b.ggmlv3.q8_0.bin", cache_dir="./") # GGUF(CPU 사용) / GPTQ(GPU 사용)
>>> quit()

================================================================================
MS, LLM보다 추론 능력 뛰어난 sLLM '오르카 2' 출시

마이크로소프트(MS)가 경량 언어모델(sLLM) ‘오르카 2(Orca 2)’를 공개했다. 놀라운 것은 70억 및 130억개의 매개변수를 가진 경량 모델로, 매개변수가 5~10배 더 큰 대형언어모델(LLM) 보다 뛰어난 추론 능력을 보인다는 점이다. 23년11월21일(현지시간) 벤처비트에 따르면 오르카 2는 130억 매개변수의 ‘오르카’ 모델을 기반으로 한 70억 매개변수의 ‘오르카 2-7B’와 130억 매개변수의 ‘오르카 2-13B’ 두가지로 출시됐다. MS는 "오르카 2의 개선된 훈련 방법이 더 작은 언어 모델이 일반적으로 훨씬 더 큰 언어 모델의 추론 능력을 능가할 수 있다는 것을 입증한다"라고 주장했다. 오르카 2는 ‘라마 2(Llama 2)’ 기반 모델을 고도로 맞춤화된 합성 데이터셋에서 미세조정했다.

데이터셋은 오르카 2에게 단계별, 회상 후 생성, 회상-이유-생성, 직접 답변 등 다양한 추론 기술을 가르치고, 동시에 각 작업에 대해 가장 효과적인 추론 기술을 결정하는 방법을 훈련했다. 오르카 2 모델은 언어 이해, 상식 추론, 다단계 추론, 수학 문제 해결, 독해, 요약 및 진실성 등 15개의 다양한 주제를 다루는 일련의 벤치마크에서 크기가 5~10배 더 큰 ‘라마 2’ 및 ‘위저드LM(WizardLM)’보다 뛰어난 성능을 보였다. 오르카 2 7B 및 13B는 모든 벤치마크 결과에서 평균적으로 '라마-2-챗-13B/70B' 및 '위저드LM-13B/70B'보다 우수한 것으로 나타났다.

MS는 “오르카 2의 성능이 비슷한 크기의 모델을 훨씬 능가하고 최소 10배 이상 큰 모델과 유사하거나 더 나은 성능을 달성, 작은 모델도 나은 추론 능력을 제공할 수 있는 가능성을 보여준다”라며 “미세조정을 위해 신중하게 필터링한 합성 데이터를 사용한 것이 개선의 핵심”이라고 설명했다. MS는 오르카 모델을 만드는 데 사용된 기술이 다른 기반 모델에도 사용될 수 있다고 덧붙였다. 

출처 : AI타임스(https://www.aitimes.com)
================================================================================



PS C:\AI\llama2_cpu_inference_@_wwhss> python wwhss.py --query "Who is Holy Spirit?"
================================================================================
Answer:
The Holy Spirit is God's divine breath that brings new life to those who are born again through faith in Jesus Christ. Just as the wind blows where it wishes and cannot be controlled, so too is the work of the Holy Spirit beyond human comprehension. While we may not know exactly where the Holy Spirit comes from or where it goes, we can trust that it is at work in the world, bringing about the transformation of those who are born again through faith in Jesus Christ.
================================================================================
Reference text:
John 3:7 Do not marvel that I said to you, 'You must be born again.'
John 3:8 The wind blows where it wishes, and you hear the sound of it, but cannot tell where it comes from and where it goes. So is everyone who is born of the Spirit.
John 3:9 Nicodemus answered and said to Him, How can these things be?
John 3:10 Jesus answered and said to him, Are you the teacher of Israel, and do not know these things?
John 3:11 Most assuredly, I say to you, We speak what We know and testify what We have seen, and you do not receive Our witness.
John 3:12 If I have told you earthly things and you do not believe, how will you believe if I tell you heavenly things?
Source data:
wwhss_data\Holy Bible - NKJV Version
================================================================================
Time(in seconds) to retrieve the answer: 62.874891500000004
PS C:\AI\llama2_cpu_inference_@_wwhss>

# 영어성경 5개 DB 구축 : 80 MBytes, 20 Minutes
PS C:\AI\llama2_cpu_inference_@_wwhss> python .\wwhss_db.py
Time(in seconds) to generate vector db: 1159.4997665
PS C:\AI\llama2_cpu_inference_@_wwhss> 

=======================
= 5 Bibles in English =
=======================

Holy Bible - KJV Version
The Holy Bible, King James Version (KJV) Copyright 1611 by King James I of England. No rights reserved.

Holy Bible - NKJV Version
The Holy Bible, New King James Version (NKJV) Copyright 1982 by Thomas Nelson. All rights reserved.

Holy Bible - NIV Version
The Holy Bible, New International Version (NIV) Copyright 1984 by Biblica Inc. All rights reserved.

Holy Bible - NLT Version
The Holy Bible, New Living Translation (NLT) Copyright 1996 by Tyndale House Foundation. All rights reserved.

Holy Bible - BBE Version
The Holy Bible in Basic English, Translated by Professor S. H. Hooke using a total of 1,000 words, Since 1949
