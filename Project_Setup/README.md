# Planning & Project Setup

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
        
2. Data collection & labeling
    * EDA
    * Domain knowledge
    * SQL like crazy

3. Training and debugging
    * Keep the first model simple and get the infrastructure right
    * Model of increasing complexity
    * Interpretable
    
4. Evaluation
    * Metric definition
    
5. Deployment. 

6. Monitoring.
    
********

# ML in production doc

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

********

# Bookings paper:
https://dl.acm.org/doi/10.1145/3292500.3330744

Leassons learned at booking:

#### INCEPTION: MACHINE LEARNING AS A SWISS KNIFE FOR PRODUCT DEVELOPMENT

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

#### "MODELING: OFFLINE MODEL PERFORMANCE IS JUST A HEALTH CHECK!":
Offline model performance metrics are only a health check, to make sure the algorithm does what we want to.

Click Through Rate because we know that CTR has a strong correlation or even causation with Conversion Rate, the business metric we really care about in this case. But as models get better and better, they might end up “just driving clicks”, without any actual effect on conversion. Over-optimizing proxies leads to distracting the user away from their goal.

#### MODELING: BEFORE SOLVING A PROBLEM, DESIGN IT

Problem Construction Process, qualitative aspects of a model (like diversity, transparency, adapt- ability, etc.), experiment design and latency. As an example consider a recommender system that predicts the rating a user would give to an accommodation. Minimizing RMSE looks like a reasonable approach. After a few successful iterations we hypothesize that the model is lacking diversity, so we create a challenger model that although still minimizes RMSE, somehow produces higher diversity. It is likely that this new model has a higher RMSE, but as long as it succeeds at increasing diversity and gives a reasonable RMSE, it will be used to test the hypothesis “diversity matters”. Inconclusive re- sults might point to adjustments of the model or experiment design, to make sure we give the hypothesis a fair chance. Negative results will likely reject the concept. Positive results on the other hand, will encourage diversity related changes, not only in the model but also in the User Interface, and even the product as a whole.

###### Problem setup:

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

#### DEPLOYMENT: TIME IS MONEY:
 Lattency is its own thing. Maybe more important than any business metric
 
#### MONITORING: UNSUPERVISED RED FLAGS
 
what can we say about the quality of a model by just looking at the predictions it makes when serving?
The method is based on the Response Distribution Chart (RDC), which is simply a histogram of the output of the model. The simple observation that the RDC of an ideal model should have one peak at 0 and one peak at 1 (with heights given by the class proportion) allows us to characterize typical patterns that signal potential issues in the model, a few examples are:
• A smooth unimodal distribution with a central mode might indicate high bias in the model or high Bayes error in the data
• An extreme, high frequency mode might indicate defects in the feature layer like wrong scaling or false outliers in the training data
• Non-smooth, very noisy distributions point to too exces- sively sparse models
• Differenceindistributionsbetweentrainingandservingdata may indicate concept drift, feature drift, bias in the training set, or other forms of training-serving skew.
• Smooth bimodal distributions with one clear stable point are signs of a model that successfully distinguishes two classes

#### EVALUATION: EXPERIMENT DESIGN SOPHISTICATION PAYS OFF

Experiment desing is also its own thing.

Triggered analysis with treatments design to isolate the causal effect of specific modeling and imple- mentation choices on business metrics.

experiment design
https://github.com/Italosayan/super_dan/blob/master/Project_Setup/Screenshot%202020-04-29%20at%2012.54.57.png

“Our success at Amazon is a function of how many experiments we do per year, per month, per week, per day” — Jeff Bezos

“One of the things I’m most proud of that is really key to our success is this testing framework … At any given point in time, there isn’t just one version of Facebook running. There are probably 10,000.” — Mark Zuckerberg

********
# Amazon paper: Managing ml projects.

##### Assesing Economic Value

The main parameter that will help you further in terms of ROI calculations of an ML project is the accuracy of the system that you need to match your expected gains. You see, any ML algorithm has the accuracy metric, which defines how precise the predictions (we told you to memorize this term) are. The accuracy you look for must enable the gains that you expect. This technique is called the impact of error costs assessment.

For example, you need about $1.4 million in annual savings from your anti-fraud solution to survive on the market. Let’s assume that your average revenue with 4,000 purchase orders per month – given the average order value $83 – is $332,000.

Before you had to pay chargebacks for 40 percent of fraudulent orders (1,600). That cost you $132,800. With the solution of 95 percent accuracy, you would compensate for 5 percent of 4,000 transactions (200), which is $16,600. Your gain is decreased expenses on chargebacks, and it accounts for $116,200. That’s $1,394,400 in savings each year. So, you need a solution to detect 95 suspicious transactions out of 100 (accuracy). The tool that can reach this threshold gets a green light.

* * * * * * * *

# Data-Informed Product Building 

## EVOLUTION OF A PRODUCT --- [Article 1](https://medium.com/sequoia-capital/evolution-of-a-product-223ce35f2179)

For strong products, the phases of growth usually resemble an S-curve 
Consumer businesses tend to proceed through these phases far more quickly than enterprise businesses
Better to have a few users who love a product
Monthly active users (MAUs) are also new users, and there is no churn or resurrection. 
(Note: the total number of active users for a given time period is the sum of retention, resurrection and new users.
Your month-over-month net user growth depends entirely on the Quick Ratio: (new users + resurrected users) / churned users.

new users, churn and resurrection

___

## MEASURING PRODUCT HEALTH ---[Article 2](https://medium.com/sequoia-capital/measuring-product-health-626b2186cece)	

Growth, Retention, Stickiness and Engagement.
ore set of users who care about it deeply?
Percentage of users engaging?

### GROWTH

Active users is the truest measure.
Cohorts of groups in glovo?
Total addressable market (TAM) 
Quickly is the product growing?
* given day is daily active users (DAU), the number of unique active users in a given week is weekly active users (WAU), and the number of unique active users in a given month is MAU.
* D/D, W/W, M/M, Y/Y changes Understanding how the number of active users changes day-over-day 

* Quick ratio of the recommender: New users, resurrected users, retained users and churned users. Between any two timestamps (t1 and t2), the change in growth = new users acquired within this time frame + users who were not active at time t1 but came back by time t2 — users who were present in time t2 but not there in time t1.
New users/MAU

### RETENTION

* When you are starting out, always build your product for this set of users, focusing on the use case that matters most to them.
* Creating a “magical moment” in which users first “get” the product 

* Once you have created the magical moment, study how users are retained. The retention tipping point is different for different products; in Facebook’s case, it was connecting to seven friends in 10 days.
* Set of users who install a product on a given day, week or month and seeing what percentage of them return 
* The D1 retention rate is D1/D0, the fraction of your cohort retained for one day. (D0 is the number of installers in a cohort, and D1 is the number in that cohort who still use the product after one day.)

![Retention](https://github.com/Italosayan/super_dan/blob/master/Project_Setup/Screenshot%202020-05-02%20at%2007.24.53.png)

### ENGAGEMENT

EBay connects sellers to buyers. In this model, you can increase engagement by focusing on the quality of the inventory available, the quantity of unique listings, the relevance of items shown to the buyer, the value of the listings, connecting the right content to the right buyer at the right time, simplifying the buying process, building trust at every step of the experience, etc. Optimizing each part of the funnel should increase overall engagement.

Number of sessions Number of sessions in a given day is another good indicator of whether your product is engaging. An increase in this metric is also the earliest indicator of whether you are achieving product-market fit.
Track inventory. 
Track contect consumption. How many pieces of content people consume relative to the inventory? Are some people inventory-constrained and thus unable to consume content?

Consider segmenting your metrics by country, device, age, gender, phone year class, connectivity class, platform, age in product, content format (video, picture, text, etc.) and content type (social, entertainment, informational, educational, etc.).

Leading and lagging indicators Imagine you start out using a product multiple times per day (multiple sessions) and spending a lot of time with it. Over time, you start getting bored with the product and your use drops off — but you are still an engaged user in many ways, visiting the product many times per week and more than twenty times per month. At this point, DAU, WAU and MAU have not yet changed.

Engaged/power users Your most-engaged users are the most important people to take care of. Keeping them happy is not really a growth concern, as they are not likely to churn. However, as mentioned in the discussion of retention above, it is ideal to target your product toward core users by making the experience easy for them and delighting them. Many of the metrics defined in this post can and should be segmented for the most-engaged users. Is the number of engaged users growing? Is their number of sessions and amount of time spent increasing? Are less-engaged users becoming more engaged? How many friends do these “power users” have? How much content do they produce? What features of the product do they use? Answers to questions like these can help build great experiences for your most-engaged group.


Engagement is the most important driver of retention. Creating a framework for what drives engagement in your product will help you identify leading indicators for changes in user behavior and inform interdiction techniques.

___

## DEFINING PRODUCT SUCCESS: METRICS AND GOALS --- [Article 3](https://medium.com/sequoia-capital/defining-product-success-metrics-and-goals-57e9cca29f9a)

One metric:  For Facebook, it is active users; for WhatsApp, it is number of sends; for eBay, it is gross merchandise; for PayPal, it is total payment volume.

Avoid ratios. If click-through rate is what you really care about, see if you can instead measure the number of clicks. However, this isn’t a hard-and-fast rule; there are many examples of companies that successfully used a ratio as the “metric that matters.”

Help your team define success.

Exchange rate between metrics

Avoid vanity and non-actionable metrics. For example, the number of likes your company gets on social media generally isn’t correlated with business results or customer success.

When choosing between multiple metrics, pick the simplest measurable metric you can move. For example, if your number of advertisers is correlated with your revenue, and the number of advertisers is easier to measure and move, choose the number of advertisers. You can always establish an exchange rate to determine the impact from one metric to another. Likewise, if you are ultimately interested in a metric that has a low sample size or takes a long time to measure, consider instead choosing a correlated metric to measure.

Pick the metric that most closely represents the usage of your product. For a company like Facebook and Instagram, for example, the single most important metric is active users. To measure growth at such a company, we could pick one of several active user metrics, such as daily, weekly or monthly active users (DAU, WAU or MAU), all of which are typically correlated. Choose based on the expected usage of the product. For example, if you expect the product to be used once per day or more, select DAU as your top-level metric. If instead you think the product will be used only on a weekly basis (e.g., when searching for specific restaurants, businesses, etc.), then choose WAU. One of these three — DAU, WAU or MAU — is a top-line metric for most consumer companies.

Choose a simple metric that connects to your drivers. Let’s say you are looking to increase new user acquisitions. You send emails to potential customers, and a fraction of them visit your landing page. A smaller group of users then sign up, and an even smaller group become active users. From these numbers, we can create a simple framework to think about the problem of user activation (as seen below). You can increase the total number of users who activate by increasing any of the four terms above. For example, if you see the largest drop-off among people who visit the site but do not sign up, it may make sense to set the percentage of site visitors who then sign up as your metric to move.

Consider counter-metrics if needed. In the eBay example above, useful counter-metrics include the number of unique items sold and unique inventory listed.

Product or business aspirations: Most long-term goals are based on the company’s mission. For example, if your company is in the video space, you might aspire to have the fastest-growing share of time spent on video. If you want to achieve that goal in x years, you can then break it into chunks to determine the growth you’ll need over the next y months in order to stay on track.

Product metrics: If your product has been around for a while, you can do a “bottom-up” forecasting exercise to determine your goal for your top-line metric over a given period of time. For example, a forecast of MAUs could consider historical data on seasonality, platform, country, penetration and product changes. 

New products: If your product is completely new, it will be useful to look at external benchmarks and set “top-down” goals. 

Setting goals:

Pick goals that are time-bound. Set a time frame, such as hitting the goal by the beginning of Q1 or the end of the year. You cannot hold people accountable to a goal that isn’t time-bound.

Set different goals for different time frames. Choose a long-term, aspirational goal that aligns with your vision and mission for the company, as well as more tangible, short-term goals needed to reach that point. How you frame the short-term goals should depend on how your product team operates, as well as on the time frames over which you evaluate business results. For example, some companies operate on a quarterly cycle, while others run on a half-yearly or even yearly cadence. Your goals should reflect these different time frames, and your team should execute primarily on the short-term goals.

Set two goals: an 80–20 and a 50–50. 80–20 goals are the ones you have an 80 percent chance of achieving. These goals are attainable, and hitting them will motivate the team. However, they will not help the team stretch and perform at a higher level. Therefore, it’s also important to set 50–50 goals, which you have only a 50 percent chance of achieving. While these goals are more challenging, they are also far more satisfying to reach. Whatever you do, don’t “sandbag” by setting only goals you can easily achieve. Failing to set the bar high can lead to complacency on the team and a decline in the product. If you find you always reach or exceed your 80–20 or especially your 50–50 goals, it’s likely you have set your sights too low.

___

## FRAMEWORKS FOR PRODUCT SUCCESS --- [Article 4](https://medium.com/sequoia-capital/frameworks-for-product-success-aff3f29c2c57)

Requirements of good projects:
Product-market fit, positive unit economics, and the ability to scale and grow.

Positive unit economics require careful attention to the fundamental financial building blocks of the business.

Facebook has 3 factors: growth, engagement and monetization.

![Facebook Model](https://github.com/Italosayan/super_dan/blob/master/Screenshot%202020-05-02%20at%2020.04.54.png)

From funnel to formula:
![Funnel formula](https://github.com/Italosayan/super_dan/blob/master/Project_Setup/1_ZHMq-fOV2K_BIYiYIDO7og.png)

Tips for building frameworks: 

* Understand the phenomenon and build the right model
* Know the outcome
* Identify building blocks
* Create a formula

___

## LEVERAGING DATA TO BUILD CONSUMER PRODUCTS --- [Article 5](https://medium.com/sequoia-capital/leveraging-data-to-build-consumer-products-fe9ea1a059b8)

Context:
![Analytics](https://github.com/Italosayan/super_dan/blob/master/Project_Setup/framework_analytics.png)

Defining key north star metrics and goals for products; creating a scalable data-informed organizational structure; and deeply understanding how to drive sustainable growth, retention, stickiness, engagement and monetization for products

* Goals and Metrics: Metrics encapsulate vision and mission. Goals connect vision and mission with strategy
* Organizational structure comes from the formula.
* Product level:
   * Product over time
   *  We discuss how to grow sustainably here and show that it depends on two key factors: product-market fit and positive net growth. Retention is the best way to measure product-market fit and by far the best lever for product growth. Without retention, a growing product will eventually be left with no users.
   * Engagement is the most important driver of both retention and sustainable growth.
   
___

## ENGAGEMENT DRIVES STICKINESS DRIVES RETENTION DRIVES GROWTH --- [Article 6](https://medium.com/sequoia-capital/engagement-drives-stickiness-drives-retention-drives-growth-3a6ac53a7a00)

![Engagement Machine](https://github.com/Italosayan/super_dan/blob/master/Project_Setup/engagement_model.png)

###### GROWTH: number of users relative to the total addressable market — and with respect to the balance between new user acquisition, churn and resurrection.

###### RETENTION: the measure of people who tried the product and liked it enough to return.

> percentage of users who take a given action such as logging in or sending a message within a certain period of time following sign-up.

> dollars spent within a certain period of time after the user’s first spend

###### Stickiness is about them returning of their own volition

> For example, Facebook is sticky because of users’ urge to share, and because of their curiosity about other people’s lives.
> Lness This is the number of days visited in a given time frame. Number of days visited per week 

###### Engagement: Sessions

Engagement(Sessions, actions) drives Stickiness(Lness)
The more a user engages with a product, the more sticky it becomes for them, and the more likely they are to retain.

![Engagement Model](https://github.com/Italosayan/super_dan/blob/master/Project_Setup/engagement_model.png)
 
___

## ENGAGEMENT --- [Article 7](https://medium.com/sequoia-capital/engagement-2ee11568eb88)

Not all sequeoia matters:
1. [x] https://medium.com/sequoia-capital/evolution-of-a-product-223ce35f2179
2. [x] https://medium.com/sequoia-capital/measuring-product-health-626b2186cece
3. [x] https://medium.com/sequoia-capital/defining-product-success-metrics-and-goals-57e9cca29f9a
4. [x] https://medium.com/sequoia-capital/frameworks-for-product-success-aff3f29c2c57
5. [x] https://medium.com/sequoia-capital/leveraging-data-to-build-consumer-products-fe9ea1a059b8
6. [x] https://medium.com/sequoia-capital/engagement-drives-stickiness-drives-retention-drives-growth-3a6ac53a7a00
7. [ ] https://medium.com/sequoia-capital/engagement-2ee11568eb88
8. [ ] https://medium.com/sequoia-capital/engagement-part-i-introduction-to-activity-feeds-975543cd7017
9. [ ] https://medium.com/sequoia-capital/engagement-part-2-content-production-4f2445899dbd
10. [ ] https://medium.com/sequoia-capital/engagement-part-iii-connections-and-inventory-de90533528b3
11. [ ] https://medium.com/sequoia-capital/engagement-part-iv-activity-feed-ranking-40d786b9d479
12. [ ] https://medium.com/sequoia-capital/engagement-part-v-consumption-d8ee03452a83
13. [ ] https://medium.com/sequoia-capital/engagement-part-vi-feedback-a703146d9f58
14. [ ] https://medium.com/sequoia-capital/engagement-part-vii-summary-and-product-implications-3b9e2044b328
15. [ ] https://medium.com/sequoia-capital/engagement-professional-content-part-1-content-production-e5310810847c
16. [ ] https://medium.com/sequoia-capital/engagement-professional-content-part-2-recommendations-5a8d6bf3bb8e
17. [ ] https://medium.com/sequoia-capital/engagement-professional-content-part-3-content-consumption-ab5858df19c7
18. [ ] https://medium.com/sequoia-capital/two-sided-marketplaces-and-engagement-ded7d5dcfe71

___

Why data science matters:
A company’s ability to compete is now measured by how successfully it applies analytics to vast, unstructured data sets across disparate sources to drive product innovation.

Douglas Eck, a Principal Scientist at Google AI, made the transition from academia in 2010. Since then, he has talked about an important mental shift that needs to occur during the leap — one that took him several years to achieve.
In the words of Eck, “The main mental flip is to put in a lot of energy to understand the problem without assuming the research skills you have will matter at all. Some people lead with a research solution. And sometimes an honest solution doesn’t really need AI.”
