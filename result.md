
# < TECHNICAL >

# === Ruby ===


# === Node.js, Vue.js===
## 1. 

# === AWS ===

# === Python ===
## 2. 

# === Test Development ===
## 3. 


3. Imagine a system that consists of a server and a client, which are connected over the network.   
The client sends a request, the server processes the request and sends back a response, 
and the client receives the response and processes it (e.g., check if the request was successful, process data that came from the server).  
Given this system, develop a test plan in terms of what to test, how to test, how to verify the system, etc.

[Client]-----[Network]-----[Server]

Format: 
1-1. Test Case Name
1-2. Test Scope
1-3. Test Steps 
1-4. Comments 

- 2-1 리스트 생성하는 웹 어플리케이션이지? 이것의 Block diagram 을 그려봐 줄래? 단순히 client - server 가 아니고, 프로세서 개념으로 그려 봐줄래? 
  (참고로 processor 는 어떤 프로그램 일 수도 있고, object 가 만들어져서 프로그램 안에서 돌아가는 thread 일 수도 있어. 가령, input 은 어떤 함수가 받고, 그것을 클릭하면 어떤 프로세서가 이 event 를 듣고, 
   서버에서는 어떤 프로세서 (혹은 이 프로세서 안에 있는 어떤 함수?) 가 request 를 받으며, 디스플레이는 누가 맡고 있는지. 또한 add, delete  할때 flow 가 어떻게 일어나는지  diagram 을 그려보라는 뜻) 

- 2-2 위에 그린 diagram 을 기반으로 테스트 플랜을 짜줄 수 있어? 
  (참고로 테스트 플랜을 말할때는 처음에는 manual test 를 말해. 그렇게 하고 나서 자동화 시키는 것이 (CI/CD 에서 돌아가도록) automation 이지) 
예를 들면, 이렇게 하는 것을 말해. 

client ----- server  이런 그림이 있다고 할때, 테스트 플랜을 다음과 같이 짜볼 수 있겠지. (밑에 예는 동서가 만든 엡과는 관련이 없고, 예시를 들기 위한 것 뿐, 하지만 test name, test steps 은 동일 하게 적용이 되. 
그러니 숙제를 할때, 이 두가지 항목은 지키되, 테스트 스텝에 관해서는 동서가 2-1 답변을 어떻게 하느냐에 따라 달려있겠지?)

Test 1 name: Test client connection 
Test steps: 
1) Open terminal on client 
2) Execute the following command:
$ ping <server name> -c 4 
3) Verify ping test passes for the server 

Test 2 name: Test an existing URI on server 
Test steps: 
1) Open terminal on client 
2) Execute the following command: 
curl -X get <server name>/URI/PATH 
3) Verify the GET command returns positive   

Test 3 name: Test a bad URI on server
Test steps: 
1) Open terminal on client 
2) Execute the following command: 
curl -X get <server name>/non-existing/URI/PATH 
3) Verify that the server returns an error code (e.g. 404) in a proper way 


<br/>
<hr/>
<br/>

## 3a.

3a. Based on the test suite developed above, please come up with a regular testing template. 
For instance, this template is for a repeated testing practice which may include some test setup and teardown steps. 
It may also include some troubleshooting guidelines based on the test suite developed above. 
Hence, a tester will use this template for an ongoing testing efforts with the diagram mentioned in question 1. 


<br/>
<hr/>
<br/>

# < NON-TECHNICAL >
# === Test Artifact Management ===

## 4a. 

```javascript
const expect = require('chai').expect
const addTwoNumbers = require ('./add-two-numbers')
const LinkedList = require ('./lib/linkedList')
const helper = require ('./lib/helper')


describe("AddTwoNumbers", function (arr) {
    let linkedList1, linkedList2

    beforeEach(function() {
        linkedList1 = new LinkedList();
        linkedList2 = new LinkedList();
    });

    it("#1 [0], [0] => [0]", function () {
        linkedList1.add(0)
        linkedList2.add(0)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(0);
    });

    it("#2 [9,9,9], [9,9] => [8,9,0,1]", function () {
        linkedList1.add(9)
        linkedList1.add(9)
        linkedList1.add(9)
        linkedList2.add(9)
        linkedList2.add(9)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(1098);
    });

    it("#3 [2,4,3], [0] => [2,4,3]", function () {
        linkedList1.add(2)
        linkedList1.add(4)
        linkedList1.add(3)
        linkedList2.add(0)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(342);
    });

    it("#4 [2,4,3], [5] => [7,4,3]", function () {
        linkedList1.add(2)
        linkedList1.add(4)
        linkedList1.add(3)
        linkedList2.add(5)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(347);
    });

    it("#5 [2,4,3], [8,5] => [0,0,4]", function () {
        linkedList1.add(2)
        linkedList1.add(4)
        linkedList1.add(3)
        linkedList2.add(8)
        linkedList2.add(5)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(400);
    });

    it("#6 [2,4,3], [8] => [0,5,3]", function () {
        linkedList1.add(2)
        linkedList1.add(4)
        linkedList1.add(3)
        linkedList2.add(8)
        expect(helper(addTwoNumbers(linkedList1, linkedList2))).to.equal(350);
    });
  });
  

```

<br/>
<hr/>
<br/>

## 4b. 

<br/>
<hr/>
<br/>

## 5. 

<br/>
<hr/>
<br/>

## 6. 

<br/>
<hr/>
<br/>

## 7. 

<br/>
<hr/>
<br/>

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

        Deliverables: Test Strategy document, Test Plan, and Test Effort estimation document.


3.  Test Design(Test case development)

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


6.  Test Closure

        The final stage where we prepare Test Closure Report, Test Metrics.
        The testing team will be called out for a meeting to evaluate cycle completion criteria based on Test coverage, Quality, Time, Cost, Software, Business objectives.
        The test team analyses the test artifacts (such as Test cases, Defect reports, etc.,) to identify strategies that have to be implemented in the future, which will help to remove process bottlenecks in the upcoming projects.
        Test metrics and Test closure report will be prepared based on the above criteria.

        Deliverables: Test Closure report, Test metrics

<br/>
<hr/>
<br/>

## 8a. 

1.  Requirement Analysis - BRS(Business Requirement Specification) documents
2.  Test Planning - Requirements Documents
3.  Test Design(Test case development) - Requirements Documents (Updated version of unclear or missing requirement)
4.  Test Environment Setup - Test Plan, Test environment setup plan, Smoke Test cases, Test Data
5.  Test Execution - Test Plan document, Test cases, Test data, Test Environment
6.  Test Closure - Test Case Execution report (make sure there are no high severity defects opened), Defect report

<br/>
<hr/>
<br/>

| STLC Phase | Documentation	| Deliverables |
| :----------: | :-------------- | :------------ | 
| Requirement Analysis | Business Requirements specification document<br/> Acceptance criteria document<br/> Application architectural document | List of all testable requirements<br/> Automation feasibility report (if applicable) |
| Test Planning | Requirements Documents<br/> Automation feasbility report | Test Strategy document<br/> Test Plan<br/> and Test Effort estimation document |
| Test Design<br/>(Test case development)	| Requirements Documents (Updated version of unclear or missing requirement)<br/> RTM(Requirement Traceability Matrix)<br/> Test Plan<br/> Test Estimation Document<br/> Automation Analysis Report | Test cases<br/> Test Scripts (if automation)<br/> Test data |
| Test Environment Setup | Test Plan<br/> Test environment setup plan<br/> Smoke Test cases<br/> Test Data | Test Environment<br/> Smoke Test Results |
| Test Execution | Test Plan document<br/> Test cases<br/> Test Scripts<br/> Test data<br/> Test Environment | Test case execution report<br/> Defect reports<br/> RTM(Requirement Traceability Matrix) |
| Test Closure | Testing has been completed<br/> Test Case Execution report (make sure there are no high severity defects opened)	| Test Closure report<br/> Test metrics |


