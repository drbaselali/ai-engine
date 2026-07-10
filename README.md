# ai-engine

A collection of applications and functions in prompt and AI engineering using Python.

Current project titled **"Core AI Pipeline Components"**

This project implements local large language model (LLM) inference, query-based information extraction, context compression, and response generation based on provided evidence using raw LLM models via Ollama. Furthermore, after response generation, the pipeline continues by extracting claims and classifying them, which then allows the model to evaluate these claims and produce a recommendation summary.

**Project Workflow**

* Provide stored or live query-relevant links
* Pass the links to an Ollama local model (extractor model)
* Produce relevant knowledge summaries
* Pass the summaries to a second Ollama model (generator model)
* Produce the required response
* Extract atomic claims
* Classify the extracted claims
* Review the response and claims and produce recommendations summary

The details of the project and its functions are provided in src. This project demonstrates the following capabilities:

* Prompt engineering
* Local AI deployment
* Multi-step LLM orchestration
* Evidence-based AI systems

# Application Example

* User prompt: Describe WWII
* Sources:
  
1- https://www.wikiwand.com/en/World_War_II

2- https://www.britannica.com/event/How-Did-World-War-II-Start

3- https://commons.wikimedia.org/wiki/Atlas_of_World_War_II

4- https://timepath.org/world-war-ii

5- https://www.imdb.com/title/tt40385200/

6- https://www.cbsnews.com/tag/world-war-ii/

7- https://www.politico.com/news/world-war-ii

* Generated response using the extracted summaries from the sources:
World War II was a global conflict that lasted from 1939 to 1945 and involved most of the world's nations. It began on September 1, 1939, when Germany invaded Poland, leading Great Britain and France to declare war two days later. The immediate causes were rooted in the harsh terms of the Treaty of Versailles after World War I, which left Germany economically crippled and politically humiliated, fostering resentment that allowed Adolf Hitler and the Nazi Party to rise to power.

Key events include:
- Operation Barbarossa (June 22, 1941): The German invasion of the Soviet Union.
- Pearl Harbor Attack (December 7, 1941): A surprise military strike by Japan against the United States naval base at Pearl Harbor, Hawaii, which led to America's entry into the war.
- D-Day Invasion (June 6, 1944): The Allied invasion of Normandy in France, marking a significant turning point for Allied forces.

The conflict involved major powers such as the Allies (United States, United Kingdom, Soviet Union) and Axis Powers (Nazi Germany, Fascist Italy, Imperial Japan). Notable leaders included Adolf Hitler, Winston Churchill, Franklin D. Roosevelt, and Joseph Stalin. The war resulted in an estimated 70 million fatalities, including millions of military and civilian deaths.

Significant battles include the Battle of Stalingrad, a turning point on the Eastern Front, and the Battle of Midway, which weakened Japan's naval capabilities. Other notable events are the Holocaust, where six million Jews were systematically murdered by Nazi Germany, and the atomic bombings of Hiroshima and Nagasaki in 1945, leading to Japan's unconditional surrender.

The war had profound impacts on geopolitics and society, reshaping the world order after its end. Memorials and remembrance events continue to honor veterans and remember the sacrifices made during World War II. Modern discussions often draw parallels between current political situations and historical figures like Adolf Hitler, emphasizing the importance of learning from past conflicts.

The provided sources also highlight various aspects such as military operations, political boundaries, strategic locations, and technological advancements through detailed maps and annotations in atlases dedicated to World War II. Documentaries and modern media continue to explore and document the events and legacy of this global conflict.

* Extracted atmoic claims: 
1. World War II was a global conflict that lasted from 1939 to 1945
2. The conflict began on September 1, 1939, when Germany invaded Poland
3. Great Britain and France declared war two days after Germany's invasion of Poland
4. The immediate causes were rooted in the harsh terms of the Treaty of Versailles after World War I
5. Adolf Hitler and the Nazi Party rose to power due to resentment fostered by the Treaty of Versailles
6. Operation Barbarossa was the German invasion of the Soviet Union on June 22, 1941
7. The Pearl Harbor Attack occurred on December 7, 1941
8. The United States entered the war after the Pearl Harbor Attack
9. D-Day Invasion took place on June 6, 1944
10. Allied forces invaded Normandy in France during D-Day
11. Major powers involved were the Allies (United States, United Kingdom, Soviet Union) and Axis Powers (Nazi Germany, Fascist Italy, Imperial Japan)
12. Notable leaders included Adolf Hitler, Winston Churchill, Franklin D. Roosevelt, and Joseph Stalin
13. The war resulted in an estimated 70 million fatalities
14. Six million Jews were systematically murdered by Nazi Germany during the Holocaust
15. Atomic bombings of Hiroshima and Nagasaki occurred in 1945
16. Japan's unconditional surrender followed the atomic bombings
17. World War II had profound impacts on geopolitics and society, reshaping the world order after its end

* Claims classification:
1. [R] World War II was a global conflict that lasted from 1939 to 1945
2. [R] The conflict began on September 1, 1939, when Germany invaded Poland
3. [R] Great Britain and France declared war two days after Germany's invasion of Poland
4. [E] The immediate causes were rooted in the harsh terms of the Treaty of Versailles after World War I
5. [R] Adolf Hitler and the Nazi Party rose to power due to resentment fostered by the Treaty of Versailles
6. [R] Operation Barbarossa was the German invasion of the Soviet Union on June 22, 1941
7. [R] The Pearl Harbor Attack occurred on December 7, 1941
8. [R] The United States entered the war after the Pearl Harbor Attack
9. [R] D-Day Invasion took place on June 6, 1944
10. [R] Allied forces invaded Normandy in France during D-Day
11. [R] Major powers involved were the Allies (United States, United Kingdom, Soviet Union) and Axis Powers (Nazi Germany, Fascist Italy, Imperial Japan)
12. [R] Notable leaders included Adolf Hitler, Winston Churchill, Franklin D. Roosevelt, and Joseph Stalin
13. [E] The war resulted in an estimated 70 million fatalities
14. [R] Six million Jews were systematically murdered by Nazi Germany during the Holocaust
15. [R] Atomic bombings of Hiroshima and Nagasaki occurred in 1945
16. [R] Japan's unconditional surrender followed the atomic bombings
17. [E] World War II had profound impacts on geopolitics and society, reshaping the world order after its end

* Recommendations:

- "The war resulted in an estimated 70 million fatalities."

*Explanation:* This claim is highly debated among historians due to varying methodologies for estimating casualties. The number can vary significantly based on sources and the inclusion of different groups (e.g., civilians, military personnel).

*Improvement Suggestion:* Provide a range or cite specific sources that support this estimate.

- "World War II had profound impacts on geopolitics and society, reshaping the world order after its end."

*Explanation:* While generally accurate, this statement is broad and lacks specificity. It does not detail how exactly the world order was reshaped, which could be elaborated upon for better clarity.

*Improvement Suggestion:* Specify key geopolitical changes such as the formation of the United Nations, the division of Germany, or the rise of the Cold War between the USA and USSR.

- "The immediate causes were rooted in the harsh terms of the Treaty of Versailles after World War I."

*Explanation:* While the Treaty of Versailles did contribute to post-war resentment, it is an oversimplification to state that its harsh terms were the sole or primary cause. Other factors such as economic instability and political turmoil also played significant roles.

*Improvement Suggestion:* Include additional context about other contributing factors like the Great Depression, which exacerbated existing tensions.


- "Adolf Hitler and the Nazi Party rose to power due to resentment fostered by the Treaty of Versailles."

*Explanation:* Similar to the previous claim, this statement is an oversimplification. While the Treaty contributed to a climate of discontent, other factors such as economic conditions and political instability were also crucial in Hitler's rise.

*Improvement Suggestion:* Provide more context on how various social, economic, and political factors combined to create an environment where the Nazi Party could gain power.

- "The United States entered the war after the Pearl Harbor Attack."

*Explanation:* While this is true, it might be more accurate to specify that the U.S. declared war on Japan following the attack and subsequently also declared war on Germany due to its involvement in Europe.

*Improvement Suggestion:* Clarify that the U.S. declared war on both Japan and Germany after Pearl Harbor.

# Further Steps
* Reducing LLM-model dependence where possible with statistical scoring or fixed text templates.
* Expermenting with different prompts accross different fields of knowledge
* Observe and document hallucination cases when detected
  
Author

Dr. Basel Ali

