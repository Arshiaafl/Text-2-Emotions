from transformers import pipeline

summarizer = pipeline('summarization')

article = """
In recent years, the rapid advancement of artificial intelligence (AI) has transformed numerous sectors of society, reshaping the way we live, work, and interact with technology. AI, encompassing various technologies such as machine learning, deep learning, and natural language processing, has become increasingly ubiquitous, permeating industries ranging from healthcare and finance to transportation and entertainment.

One of the most significant impacts of AI is its ability to automate tasks and processes that were previously labor-intensive or time-consuming. Through sophisticated algorithms and vast amounts of data, AI systems can analyze complex patterns, make predictions, and generate insights with remarkable speed and accuracy. This has led to improvements in efficiency, productivity, and cost-effectiveness across many domains.

Moreover, AI-powered applications have revolutionized the delivery of healthcare services, enabling personalized treatment plans, early disease detection, and more efficient medical imaging analysis. In finance, AI algorithms are used for fraud detection, risk assessment, and algorithmic trading, driving innovation and efficiency in the financial markets.

However, the widespread adoption of AI has also raised concerns about ethical implications and potential biases inherent in the technology. Issues such as algorithmic fairness, transparency, and accountability have come to the forefront of discussions among researchers, policymakers, and industry leaders. Addressing these concerns is crucial to ensuring that AI systems are developed and deployed responsibly, with due consideration for the societal impacts they may have.

Despite these challenges, the pace of AI innovation shows no signs of slowing down. Breakthroughs in AI research continue to push the boundaries of what is possible, opening up new opportunities for solving complex problems and addressing pressing global challenges. From autonomous vehicles and virtual assistants to personalized recommendations and predictive analytics, AI is poised to transform virtually every aspect of human endeavor.

In conclusion, while the rise of artificial intelligence presents both opportunities and challenges, its potential to improve lives and drive innovation is undeniable. By fostering collaboration, transparency, and ethical stewardship, we can harness the power of AI to create a more inclusive, sustainable, and prosperous future for all.



"""


t = summarizer(article, max_length = 130, min_length = 30, do_sample = False)

print(t)