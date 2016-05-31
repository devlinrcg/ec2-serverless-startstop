# Stack AWS Cloudformation: Start/Stop Amazon EC2 instances using AWS Lambda
###### How it works
* Each directory in this repository represents **ONE** AWS Region. This means that templates can be launched in **ANY** AWS Region with AWS Lambda available;
    * As an example: if you have your Amazon EC2 instances on the SaoPaulo Region, you will have to launch the stack, let's say, on Virginia's Region (which will have the AWS Lambda availability), using the directory/template from SaoPaulo;
* Each directory contains one template, 2 scripts (start_all.py an stop_all.py) and onw zip_all.sh script;
* For every editing on start_all.py and/or stop_all.py, you have to execute the zip_all.sh on that directory;
* The AWS Cloudformation creates, automatically, your role and policy so you can execute your functions on AWS Lambda;

###### Usage
* Access your AWS account and go to [Amazon S3](https://console.aws.amazon.com/s3/);
* Create a Bucket, and click on it;
* Upload the **ec2-startstop.template** and **ec2-startstop.zip** from the direstory representing the AWS Region where you want to execute the Functions;
* Click on the **ec2-startstop.template**, and then on **Properties**;
* Copy the link presented to you, e.g. https://s3.amazonaws.com/SEU_BUCKET/ec2-startstop.template
* Now, go to [AWS Cloudformation](https://console.aws.amazon.com/cloudformation/);
* Click on **Create Stack**;
    * In the field **Specify an Amazon S3 template URL**, insert the link for your template (copied before), and click next;
    * Put the information needed: in **S3BucketName**, put the name of your Bucket, created earlier;
    * In **SNSTopicName**, insert a name for an AWS Push Notification Service topic to be created, which will be used to alert you in case of any error/alert on the Function execution;
    * Next, Next, Create;
    * When launched, resources will be created automatically;
    * After everything is created, go to the Management Console for AWS Push Notification Service and subscribe to the created topic, so you can receive alerts;
* Repeat these steps for different AWS Regions;
* To schedule these Functions to be executed at a time/date/rate of your choice, after launching the Stacks, insert an **Event Source** in each AWS Lambda Function, as informed below:
    * Go to [AWS Lambda](https://console.aws.amazon.com/lambda);
    * Click on the Function you want to schedule an event;
    * Click on the **Event sources** tab;
    * Click on **Add event source**;
    * On this screen:
      * Event source type: **Cloudwatch Events - Schedule**;
      * Rule name: a name for your rule;
      * Rule description: a description for your rule;
      * Schedule expression: follow the expressions below;
      * **Submit** and done;
      * Repeat these steps for each Function;

###### Expressions - Schedule an Event
Same as cron (Linux), following the UTC (+3BRT) timezone. Some examples:

* Executed at 17:00 (BRT) from monday until friday:
```
      cron(0 20 ? * MON-FRI * )
```
* Executed at 8:00 (BRT) from monday until friday:
```
      cron(0 11 ? * MON-FRI * )
```  

After you finish, insert the Tag **AutoStartStop**, with Value **TRUE** on the Amazon EC2 instances that will be part of the Stop/Start. In case any Amazon EC2 instance don't have this Tag, without the Value **TRUE**, it won't be in the Start/Stop execution.  
**TAGS ARE CASE-SENSITIVE!!!**

###### Functions
**start_all.py**: Execute the START on all Amazon EC2 instances with Tag Name AutoStartStop, and Value TRUE (CASE-SENSITIVE);  
**stop_all.py**: Execute the STOP on all Amazon EC2 instances with Tag Name AutoStartStop, and Value TRUE (CASE-SENSITIVE);
###### Files
```
ec2-serverless-startstop
├── California
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Frankfurt
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Ireland
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Oregon
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── README.md
├── SaoPaulo
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Seoul
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Singapore
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Sydney
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
├── Tokyo
│   ├── ec2-startstop.template
│   ├── ec2-startstop.zip
│   ├── start_all.py
│   ├── stop_all.py
│   └── zip_all.sh
└── Virginia
    ├── ec2-startstop.template
    ├── ec2-startstop.zip
    ├── start_all.py
    ├── stop_all.py
    └── zip_all.sh
```
