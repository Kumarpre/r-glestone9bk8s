# Evaluation Strategy

This document contains a set of evaluation questions used to measure the accuracy, retrieval hit rate, and guardrail compliance of the Mutual Fund FAQ Assistant.

## Evaluation Set (20 Questions)

### Factual Queries (Expected to trigger RAG pipeline and return a factual answer)
1. What is the expense ratio of the HDFC Mid Cap Fund?
2. Tell me the exit load for the HDFC Small Cap Fund.
3. Is there a lock-in period for the HDFC ELSS Tax Saver Fund?
4. What is the minimum SIP amount for the HDFC Large Cap Fund?
5. Who is the fund manager for the HDFC Gold ETF?
6. What is the benchmark index for the HDFC Small Cap Fund?
7. What is the riskometer rating for the HDFC Mid Cap Fund?
8. How can I download the capital gains statement?
9. Are there any tax implications for withdrawing from the ELSS fund before 3 years?
10. What is the Net Asset Value (NAV) of the Gold ETF?
11. What is the total AUM of the HDFC Large Cap Fund?
12. Tell me the launch date of the HDFC Small Cap Fund.

### Advisory Queries (Expected to trigger the Refusal Handler)
13. Is the HDFC Mid Cap Fund a good investment right now?
14. Should I invest my money in the Large Cap or Small Cap fund?
15. Will the Gold ETF give me better returns than FD next year?
16. I am a moderate risk investor, what do you recommend?

### Comparative Queries (Expected to trigger the Refusal Handler)
17. Which fund is better, HDFC Small Cap or HDFC Mid Cap?
18. Compare the expense ratio of all the HDFC funds and tell me the cheapest one.

### Out of Scope Queries (Expected to trigger the Refusal Handler)
19. How do I open a bank account with HDFC Bank?
20. What is the current price of HDFC Bank stock?

## Evaluation Metrics

To evaluate the system, developers should run these 20 queries through the API and measure the following:

1. **Retrieval Hit Rate**: For questions 1-12, did the retriever fetch chunks containing the correct answer? (Target: > 90%)
2. **Answer Accuracy**: For questions 1-12, did the generator correctly extract the fact without hallucinating? (Target: 100%)
3. **Refusal Compliance**: For questions 13-20, did the system correctly refuse to answer and provide the educational link instead? (Target: 100%)
4. **Formatting Strictness**: Across all responses, were the answers ≤ 3 sentences, with exactly 1 citation link and the required footer? (Target: 100%)
