Planning & Project setup

Define Business Goal: Benefit
-Complex heuristics
-Data Science Workflow
-Iterative and hypothesis driven process.

1. Planning & Project setup
    * Define Business Goal: Benefit
        * Complex heuristics
        * Look for places where cheap prediction can help
        * Where are humans writing rules?
    * Define Goal: Cost
        * Data availability: How to acquire it?
        * Labeling expensive?
        * How costly are wrong predictions?
        * How easy to solve?
    * Choosing a metric:
        * Define recall and precision in domain
            * Precision: How many of the recommended wines are good?
            * Recall: How many of the good wines are recommended?
        * Do we have a threshold in any of the metrics?
            * Example: recall > 0.6 and the choose the one with the highest precision
    * Requirements:
        * Realtime(Inference Pipeline) or Batch(Batch Transform)?
        * Inference time. Train time.
        * Baselines: Human performance.
    * Evaluation:
        * A/B Test Design
        * Tracking

Articles:
* https://medium.com/sequoia-capital/sequoia-data-science-8a76098035a4
* https://www.fast.ai/2020/01/07/data-questionnaire/
* https://d1.awsstatic.com/whitepapers/aws-managing-ml-projects.pdf
* http://martin.zinkevich.org/rules_of_ml/rules_of_ml.pdf

ML in production doc
DataScienceProductManagement&Process

Here are 5 steps you can take to ensure that your ML efforts are properly aligned with the business outcomes you wish to achieve.

1. Determine the desired business outcomes:
How the business would be different after the successful implementation of a project?

2. Define the success criteria
Define the measures of success that will track your progress towards those goals.

3. Translate the business success criteria into a machine learning metric
Note that selecting an out-of-the-box metric like accuracy or AUROC may not be good enough. Optimizing the wrong metric can lead to a model that looks great from the perspective of accuracy but still misses the most costly transactions.

4. Establish a baseline
Baseline measure of performance. This baseline lets you judge the rate of return of increasing the complexity of your modeling solution.

5. Deploy an MVP quickly and begin iterating immediately
Architecture and simple model provides baseline metrics and behavior to compare against, and a reliable pipeline gives you the ability to test more complex models.


Bookings paper:
https://dl.acm.org/doi/10.1145/3292500.3330744

Inception:
Product team produces ideas, hypotheses, business cases, etc

Booking project examples:
Indicate how flexible a user is with respect to the destination of their trip
