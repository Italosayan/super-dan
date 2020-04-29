Planning & Project setup

Data Science Workflow :Iterative and hypothesis driven process.

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

Models that solve size of the glovo bubble vs "semantic layer" models that define metrics to use across the business.
Concretely, in our analysis we found that on average each semantic model generated twice as many use cases as the specialized ones.

"Model Categories"
-Traveller Preference Models: Flexible on dates or not?
-Traveller Context Models: Family? Multi city? Constraints and requirements.
-Item Space Navigation Models: scrolling, clicking, sorting, filtering.
-Interface Optimization Models: Use content to define user interface.
-Content Curation: Simplify images, reviews, etc.
-Content Augmentation:  augmentation is about enriching an existing entity using data from many others. 
   *"Great Value Today" icons simplify this process by highlight- ing properties offering an outstanding value for the price  they are asking. Also: price trends to help the user

"MODELING: OFFLINE MODEL PERFORMANCE IS JUST A HEALTH CHECK!":
Offline model performance metrics are only a health check, to make sure the algorithm does what we want to.

Click Through Rate because we know that CTR has a strong correlation or even causation with Conversion Rate, the business metric we really care about in this case. But as models get better and better, they might end up “just driving clicks”, without any actual effect on conversion. An example of this is a model that learned to recommend very similar hotels to the one a user is looking at, encouraging the user to click (presumably to compare all the very similar hotels), eventually drowning them into the paradox of choice and hurting conversion. In general, over-optimizing proxies leads to distracting the user away from their goal.

Inception:

Problem Construction Process, qualitative aspects of a model (like diversity, transparency, adapt- ability, etc.), experiment design and latency. As an example consider a recommender system that predicts the rating a user would give to an accommodation. Minimizing RMSE looks like a reasonable approach. After a few successful iterations we hypothesize that the model is lacking diversity, so we create a challenger model that although still minimizes RMSE, somehow produces higher diversity. It is likely that this new model has a higher RMSE, but as long as it succeeds at increasing diversity and gives a reasonable RMSE, it will be used to test the hypothesis “diversity matters”. Inconclusive re- sults might point to adjustments of the model or experiment design, to make sure we give the hypothesis a fair chance. Negative results will likely reject the concept. Positive results on the other hand, will encourage diversity related changes, not only in the model but also in the User Interface, and even the product as a whole.

Problem setup:

The point(s) at which the prediction needs to be made are often given, which fixes the feature space universe, yet the target variable and the observation space are not always given and they need to be carefully constructed. 

Could learn to predict how many different dates the user will consider applying regression to a specific dataset composed by users as observations, or to estimate the probability of changing dates by solving a classification problem.

How to compare alternative set ups:
Learnability: Tumer & Ghosh
Setups where simple models can do significantly better than trivial models are preferred.
Data to Concept Match:
Some setups use data that is closer to the concept we want to model<
Selection Bias:
constructing label and observation spaces
An un- biased problem would be based on observations that map 1 to 1 to predictions made when serving

Sample mush represent the serving population distribution.

Diagnosing selection bias is straightforward: consider a sample of the natural observation space (users or sessions in the dates flexibility case), we can then construct a classification problem that classifies each observation into the class of the observations for which a target variable can be computed and the class of the observations for which a target variable cannot be computed

Correcting for this type of bias is not obvious. Techniques like Inverse Propensity Weighting [11] and Doubly Robust [4] are helpful in some cases, but they require at least one extra model to build (the propensity model). Other approaches that have been applied successfully but not systematically are methods from the PU-Learning [9] and Semi Supervised Learning fields.
