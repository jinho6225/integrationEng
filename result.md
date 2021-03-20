
# < TECHNICAL >

## === Ruby ===


## === Node.js, Vue.js===
### 1. 

## === AWS ===

## === Python ===
### 2. 

## === Test Development ===
### 3. 


### 3a. 

# < NON-TECHNICAL >

## === Test Artifact Management ===

### 4a. 
### 4b. 

### 5. 

### 6. 

### 7. 


# Concept Questions
## 8. 

1.  Requirement Analysis
   
        The test team studies and analyzes the requirements from a testing perspective
        This Phase helps to identify whether the requirements are testable or not. If any requirement is not testable, the test team can communicate with various stakeholders(Client, Business Analyst, Tech Leads, System architects, etc) during this phase so that the mitigation strategy can be planned

        Deliverables: List of all testable requirements, Automation feasibility report (if applicable)


2.  Test Planning

        Test planning is the first step in the testing process.
        In this phase typically Test Manager/Test Lead involves determining the effort and cost estimates for the entire project. Preparation of the Test Plan will be done based on the requirement analysis.
        Activities like resource planning, determining roles and responsibilities, tool selection (if automation), training requirements, etc., carried out in this phase.

        Deliverables: Test Strategy, Test Plan, and Test Effort estimation document.


3.  Test Design

        The test team starts with test case development activity here in this phase. Testers prepares test cases, test scripts (if automation), and test data.
        Once the test cases are ready then these test cases are reviewed by peer members or team lead.
        Also, the test team prepares the Requirement Traceability Matrix (RTM). RTM traces the requirements to the test cases that are needed to verify whether the requirements are fulfilled.

        Deliverables: Test cases, Test Scripts (if automation), Test data.


4.  Test Environment Setup

        This phase can be started in parallel with the Test design phase.
        The test environment setup is done based on the hardware and software requirement list. In some cases, the test team may not be involved in this phase. The development team or customer provides the test environment.
        Meanwhile, the test team should prepare the smoke test cases to check the readiness of the given test environment.

        Deliverables: Test Environment. Smoke Test Results.

    - What is Smoke Testing in Software Testing?

        Smoke Testing is done to make sure if the build we received from the development team is testable or not. It is also called as “Day 0” check. It is done at the “build level”.
        It helps not to waste the testing time to simply testing the whole application when the key features don’t work or the key bugs have not been fixed yet. Here our focus will be on primary and core application workflow.


5.  Test Execution

        The test team starts executing the test cases based on the planned test cases. If a test case result is Pass/Fail then the same should be updated in the test cases.
        The defect report should be prepared for failed test cases and should be reported to the Development Team through a bug tracking tool for fixing the defects.
        Retesting will be performed once the defect was fixed.

        Deliverables: Test case execution report, Defect report, RTM

    - What is a defect?
  
        The variation between the actual results and expected results is known as defect.
        If a developer finds an issue and corrects it by himself in the development phase then it’s called a defect.

    - What is a bug?
  
        If testers find any mismatch in the application/system in testing phase then they call it as Bug.
        There is a contradiction in the usage of Bug and Defect. People widely say the bug is an informal name for the defect.

    - What is an error?
  
        We can’t compile or run a program due to coding mistake in a program. If a developer unable to successfully compile or run a program then they call it as an error.

    - What is a failure?
  
        Once the product is deployed and customers find any issues then they call the product as a failure product. After release, if an end user finds an issue then that particular issue is called as failure


6.  Test Closure

        The final stage where we prepare Test Closure Report, Test Metrics.
        The testing team will be called out for a meeting to evaluate cycle completion criteria based on Test coverage, Quality, Time, Cost, Software, Business objectives.
        The test team analyses the test artifacts (such as Test cases, Defect reports, etc.,) to identify strategies that have to be implemented in the future, which will help to remove process bottlenecks in the upcoming projects.
        Test metrics and Test closure report will be prepared based on the above criteria.

        Deliverables: Test Closure report, Test metrics



## 8a. 

1.  Requirement Analysis - BRS(Business Requirement Specification) documents
2.  Test Planning - Requirements Documents
3.  Test Design - Requirements Documents (Updated version of unclear or missing requirement)
4.  Test Environment Setup - Test Plan, Smoke Test cases, Test Data
5.  Test Execution - Test Plan document, Test cases, Test data, Test Environment
6.  Test Closure - Test Case Execution report (make sure there are no high severity defects opened), Defect report


| STLC Phase | documentation	| Deliverables |
| :----------: | :-------------- | :------------ | 
| Requirement Analysis | Requirements specification document, Acceptance criteria document, Application architectural document | List of all testable requirements, Automation feasibility report (if applicable) |
| Test Planning | Requirements Documents, Automation feasbility report | Test Strategy, Test Plan, and Test Effort estimation document. |
| Test Design	| Requirements Documents (Updated version of unclear or missing requirement), RTM, Test Plan, Test Estimation Document, Automation Analysis Report | Test cases, Test Scripts (if automation), Test data. |
| Test Environment Setup | Test Plan, Test environment setup plan, Smoke Test cases, Test Data | Test Environment. Smoke Test Results. |
| Test Execution | Test Plan document, Test cases, Test Scripts, Test data, Test Environment. | Test case execution report, Defect reports, RTM |
| Test Closure | Testing has been completed, Test Case Execution report (make sure there are no high severity defects opened)	| Test Closure report, Test metrics |


