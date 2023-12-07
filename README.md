# project-make-computer-read-bible

#### https://github.com/boanuge/Llama-2-Open-Source-LLM-CPU-Inference @ Github Repository <br>
PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com> conda activate base <br>
PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com> python .\db_build.py <br>
PS C:\AI\Llama-2-Open-Source-LLM-CPU-Inference_@_github.com> python .\main.py <br>
<br>
# Who is Holy Spirit?
## Answer: The Holy Spirit is God's Spirit that dwells within believers (Romans 8:9-11, 1 Corinthians 3:16). It is the third person of the Trinity, along with God the Father and Jesus Christ the Son. The Holy Spirit convicts people of sin (John 16:8-11), regenerates the hearts of believers (Titus 3:5), and empowers them to live a holy life (Galatians 5:16-26).
==================================================<br>
Source Document 1<br>
Source Text: Acts 8:16 For up to that time he had not come on any of them; only baptism had been given to them in the name of the Lord Jesus.
Acts 8:17 Then they put their hands on them, and the Holy Spirit came on them.
Acts 8:18 Now when Simon saw that the Holy Spirit was given through the touch of the Apostles' hands, he made them an offering of money, saying,
Acts 8:19 Give me this power, so that when I put my hands on anyone he may get the Holy Spirit.<br>
Document Name: data\data_5_bible_english_BBE.txt<br>
============================================================<br>
Source Document 2<br>
Source Text: 1John 4:1 My loved ones, do not put your faith in every spirit, but put them to the test, to see if they are from God: because a great number of false prophets have gone out into the world.
1John 4:2 By this you may have knowledge of the Spirit of God: every spirit which says that Jesus Christ has come in the flesh is of God:
1John 4:3 And every spirit which does not say this is not from God: this is the spirit of Antichrist, of which you have had word; and it is in the world even now.<br>
Document Name: data\data_5_bible_english_BBE.txt<br>
============================================================<br>
Time to retrieve response: 82.0618728<br>
<br>
# Who is Jesus?
## Answer: Jesus is the Christ, the Son of God.
==================================================<br>
Source Document 1 <br>
Source Text: Matthew 16:13 Now when Jesus had come into the parts of Caesarea Philippi, he said, questioning his disciples, Who do men say that the Son of man is?
Matthew 16:14 And they said, Some say, John the Baptist; some, Elijah; and others, Jeremiah, or one of the prophets.
Matthew 16:15 He says to them, But who do you say that I am?
Matthew 16:16 And Simon Peter made answer and said, You are the Christ, the Son of the living God. <br>
Document Name: data\data_5_bible_english_BBE.txt <br>
============================================================<br>
Source Document 2 <br>
Source Text: John 20:31 But these are recorded, so that you may have faith that Jesus is the Christ, the Son of God, and so that, having this faith you may have life in his name.
John 21:1 After these things Jesus let himself be seen again by the disciples at the sea of Tiberias; and it came about in this way.
John 21:2 Simon Peter, Thomas named Didymus, Nathanael of Cana in Galilee, the sons of Zebedee, and two others of his disciples were all together. <br>
Document Name: data\data_5_bible_english_BBE.txt <br>
============================================================<br>
Time to retrieve response: 52.476544000000004 <br>

<br>

## NLP KoGPT2 (마침표있는)전처리데이터.ipynb

# 예수님
## Output
예수님께서 또 말씀하셨습니다. 빛이 생겨라! 그러자 빛이 생겼습니다.
그 빛이 하나님께서 보시기에 좋았습니다. 하나님께서 빛과 어둠을 나누셨습니다.
하나님께서는 빛을 낮 이라 부르시고, 어둠을 밤 이라 부르셨습니다. 저녁이 지나고 아침이 되니, 이 날이 첫째 날이었습니다.
하나님께서 또 말씀하셨습니다. 물 한가운데 둥근 공간이 생겨 물을 둘로 나누어라.
하나님께서 둥근 공간을 만드시고, 그 공간 아래의 물과 공간 위의 물을 나누시니 그대로 되었습니다.
하나님께서 그 공간을 하늘 이라 부르셨습니다. 저녁이 지나고 아침이 되니, 이 날이 둘째 날이었습니다.
하나님께서 말씀하셨습니다. 하늘 아래의 물은 한 곳으로 모이고 뭍은 드러나라 하시니 그대로 되었습니다.
하나님께서 뭍을 땅 이라 부르시고 모인 물은 바다 라고 부르셨습니다. 하나님께서 보시기에 좋았습니다.
하나님께서 말씀하셨습니다. 땅은 풀과 씨를 맺는 식물과 씨가 든 열매를 맺는 온갖 과일나무를 내어라 하시니, 그대로 되었습니다.

## NLP KoGPT2 (마침표없는)전처리데이터.ipynb

# 예수님
## Output
예수님께서 말씀하셨습니다. 그런데 그 빛이 지금처럼 짜임새 있는 모습이 아니었고 생물 하나 없이 텅 비어 있었어요. 어둠이 깊은 바다를 덮고 있었고 빛과 그림자가 생겨라 그러자 빛의 형성이 생겼고 빛을 낮 이라 부르기로 했습니다. 저녁을 지나고 아침 이 날이 첫째 날이었어요. 하나님의 영은 물 위에서 움직이고 계셔서 물을 둘로 나누어라, 저녁과 밤을 나누고 계절의 흐름을 나누자 그래서 하늘 아래의 물은 한 곳으로 모이고, 뭍은 드러나라 하시니 그대로 되었지요. 하나, 하나, 둘, 셋. 셋째 날은 또 다른 날에 일어났습니다. 며칠 전만 해도 그랬지만 오늘만은 상황이 많이 달라 ...

# Reference
https://github.com/SKT-AI/KoGPT2

Dataset size (40GB) for pretrained model

- 한국어 위키 백과, 뉴스, 청와대 국민청원 등

Dataset size (5MB) for fine-turning

- dataset_korean_easy_for_finetuning.txt (한국어 쉬운성경)
