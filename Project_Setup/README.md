Planning & Project setup

Data Science Workflow :Iterative and hypothesis driven process.

hypothesis-model-experiment cycle

https://www.jeremyjordan.me/ml-requirements/amp/

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

Leassons learned at booking:

* INCEPTION: MACHINE LEARNING AS A SWISS KNIFE FOR PRODUCT DEVELOPMENT

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

* "MODELING: OFFLINE MODEL PERFORMANCE IS JUST A HEALTH CHECK!":
Offline model performance metrics are only a health check, to make sure the algorithm does what we want to.

Click Through Rate because we know that CTR has a strong correlation or even causation with Conversion Rate, the business metric we really care about in this case. But as models get better and better, they might end up “just driving clicks”, without any actual effect on conversion. Over-optimizing proxies leads to distracting the user away from their goal.

* MODELING: BEFORE SOLVING A PROBLEM, DESIGN IT

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

* DEPLOYMENT: TIME IS MONEY:
 Lattency is its own thing. Maybe more important than any business metric
 
* MONITORING: UNSUPERVISED RED FLAGS
 
what can we say about the quality of a model by just looking at the predictions it makes when serving?
The method is based on the Response Distribution Chart (RDC), which is simply a histogram of the output of the model. The simple observation that the RDC of an ideal model should have one peak at 0 and one peak at 1 (with heights given by the class proportion) allows us to characterize typical patterns that signal potential issues in the model, a few examples are:
• A smooth unimodal distribution with a central mode might indicate high bias in the model or high Bayes error in the data
• An extreme, high frequency mode might indicate defects in the feature layer like wrong scaling or false outliers in the training data
• Non-smooth, very noisy distributions point to too exces- sively sparse models
• Differenceindistributionsbetweentrainingandservingdata may indicate concept drift, feature drift, bias in the training set, or other forms of training-serving skew.
• Smooth bimodal distributions with one clear stable point are signs of a model that successfully distinguishes two classes

* EVALUATION: EXPERIMENT DESIGN SOPHISTICATION PAYS OFF

Experiment desing is also its own thing.

Triggered analysis with treatments design to isolate the causal effect of specific modeling and imple- mentation choices on business metrics.

experiment design
https://github.com/Italosayan/super_dan/blob/master/Project_Setup/Screenshot%202020-04-29%20at%2012.54.57.png


********
Amazon paper: Managing ml projects.

Assesing Economic Value

The main parameter that will help you further in terms of ROI calculations of an ML project is the accuracy of the system that you need to match your expected gains. You see, any ML algorithm has the accuracy metric, which defines how precise the predictions (we told you to memorize this term) are. The accuracy you look for must enable the gains that you expect. This technique is called the impact of error costs assessment.

For example, you need about $1.4 million in annual savings from your anti-fraud solution to survive on the market. Let’s assume that your average revenue with 4,000 purchase orders per month – given the average order value $83 – is $332,000.

Before you had to pay chargebacks for 40 percent of fraudulent orders (1,600). That cost you $132,800. With the solution of 95 percent accuracy, you would compensate for 5 percent of 4,000 transactions (200), which is $16,600. Your gain is decreased expenses on chargebacks, and it accounts for $116,200. That’s $1,394,400 in savings each year. So, you need a solution to detect 95 suspicious transactions out of 100 (accuracy). The tool that can reach this threshold gets a green light.

* * * * * * * *

Data-Informed Product Building 

EVOLUTION OF A PRODUCT

For strong products, the phases of growth usually resemble an S-curve 
Consumer businesses tend to proceed through these phases far more quickly than enterprise businesses
Better to have a few users who love a product
Monthly active users (MAUs) are also new users, and there is no churn or resurrection. 
(Note: the total number of active users for a given time period is the sum of retention, resurrection and new users.
Your month-over-month net user growth depends entirely on the Quick Ratio: (new users + resurrected users) / churned users.

new users, churn and resurrection

MEASURING PRODUCT HEALTH

Growth, Retention, Stickiness and Engagement.
ore set of users who care about it deeply?
Percentage of users engaging?

GROWTH

Active users is the truest measure.
Cohorts of groups in glovo?
Total addressable market (TAM) 
Quickly is the product growing?
* given day is daily active users (DAU), the number of unique active users in a given week is weekly active users (WAU), and the number of unique active users in a given month is MAU.
* D/D, W/W, M/M, Y/Y changes Understanding how the number of active users changes day-over-day 

* Quick ratio of the recommender: New users, resurrected users, retained users and churned users. Between any two timestamps (t1 and t2), the change in growth = new users acquired within this time frame + users who were not active at time t1 but came back by time t2 — users who were present in time t2 but not there in time t1.
New users/MAU

RETENTION

* When you are starting out, always build your product for this set of users, focusing on the use case that matters most to them.
* Creating a “magical moment” in which users first “get” the product 

* Once you have created the magical moment, study how users are retained. The retention tipping point is different for different products; in Facebook’s case, it was connecting to seven friends in 10 days.
* Set of users who install a product on a given day, week or month and seeing what percentage of them return 
* The D1 retention rate is D1/D0, the fraction of your cohort retained for one day. (D0 is the number of installers in a cohort, and D1 is the number in that cohort who still use the product after one day.)

https://www.oreilly.com/radar/drivetrain-approach-data-products/

Not all sequeoia matters:
https://medium.com/sequoia-capital/measuring-product-health-626b2186cece
https://medium.com/sequoia-capital/defining-product-success-metrics-and-goals-57e9cca29f9a
https://medium.com/sequoia-capital/frameworks-for-product-success-aff3f29c2c57
https://medium.com/sequoia-capital/leveraging-data-to-build-consumer-products-fe9ea1a059b8
https://medium.com/sequoia-capital/engagement-drives-stickiness-drives-retention-drives-growth-3a6ac53a7a00
https://medium.com/sequoia-capital/engagement-2ee11568eb88
https://medium.com/sequoia-capital/engagement-part-i-introduction-to-activity-feeds-975543cd7017
https://medium.com/sequoia-capital/engagement-part-2-content-production-4f2445899dbd
https://medium.com/sequoia-capital/engagement-part-iii-connections-and-inventory-de90533528b3
https://medium.com/sequoia-capital/engagement-part-iv-activity-feed-ranking-40d786b9d479
https://medium.com/sequoia-capital/engagement-part-v-consumption-d8ee03452a83
https://medium.com/sequoia-capital/engagement-part-vi-feedback-a703146d9f58
https://medium.com/sequoia-capital/engagement-part-vii-summary-and-product-implications-3b9e2044b328
https://medium.com/sequoia-capital/engagement-professional-content-part-1-content-production-e5310810847c
https://medium.com/sequoia-capital/engagement-professional-content-part-2-recommendations-5a8d6bf3bb8e
https://medium.com/sequoia-capital/engagement-professional-content-part-3-content-consumption-ab5858df19c7
https://medium.com/sequoia-capital/two-sided-marketplaces-and-engagement-ded7d5dcfe71


Why data science matters:
A company’s ability to compete is now measured by how successfully it applies analytics to vast, unstructured data sets across disparate sources to drive product innovation.
