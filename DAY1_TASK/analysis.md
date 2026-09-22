# Day 1 Task — Comparing Chatbot, Workflow and AI Agent

## 1. Scenario

The scenario is a private student placement tracker.

The system contains information about companies the student has applied to,
their application status, test completion status and interview status.

The user wants to know:

> Which companies require my next action and what should I do?

The private data is stored in `data/student_data.json`.

---

## 2. Plain Chatbot

The plain chatbot uses an LLM to answer the user's question.

The placement information is included directly in the prompt given to the
LLM.

### Flow

User question → LLM → Response

### Characteristics

- Uses an LLM for natural-language reasoning.
- Does not directly access the private JSON file.
- The required information must be provided in the prompt.
- It does not dynamically select or call external tools.

---

## 3. Rule-Based Workflow

The rule-based workflow reads the private JSON file directly.

It then applies predefined Python `if/elif/else` rules to determine the
next action.

### Flow

JSON data → Fixed rules → Result

### Example rules

- Applied + test not completed → Complete the assessment.
- Applied + test completed + no interview → Prepare for interview.
- Interview completed → Follow up.
- Offer received → Review and respond to the offer.

### Characteristics

- Predictable behavior.
- Direct access to private data.
- Easy to test and debug.
- Behavior is limited to predefined rules.
- No LLM is required.

---

## 4. AI Agent

The AI agent combines an LLM with a tool.

The agent has access to a `get_student_data` tool that reads the private
student JSON file.

### Flow

User question
→ LLM
→ Tool decision
→ get_student_data()
→ Private JSON
→ LLM
→ Final response

### Characteristics

- Can use an LLM for reasoning.
- Can access private data through a controlled tool.
- The LLM can decide when the tool is required.
- More flexible than a fixed rule-based workflow.
- Requires additional controls for tool access and reliable execution.

---

## 5. Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| LLM | Yes | No | Yes |
| Private JSON access | No | Yes | Yes, through a tool |
| Fixed rules | No | Yes | Not necessarily |
| Dynamic tool usage | No | No | Yes |
| Natural-language reasoning | Yes | Limited | Yes |
| Predictability | Depends on LLM | High for defined rules | Depends on LLM and tools |
| Flexibility | Medium | Low | High |
| Implementation complexity | Low | Low | Higher |

---

## 6. Suitability

The three approaches solve the same general problem in different ways.

The plain chatbot is useful when the required information can be supplied
directly in the conversation.

The rule-based workflow is useful when the possible situations and actions
are well defined. It provides predictable behavior but requires developers
to explicitly define the rules.

The AI agent is useful when the system needs to reason about a user's
request and access information through tools. In this scenario, the agent
can use the private placement data through `get_student_data`.

The appropriate choice depends on the required level of flexibility,
predictability, tool access and implementation complexity.

---

## 7. Implementation Status

The following components were implemented:

- Private student data stored in JSON.
- Plain chatbot implementation.
- Rule-based workflow implementation.
- `get_student_data` agent tool.
- AI agent implementation.

The OpenAI API execution could not be completed in the current environment
because the API project returned:

`credit_balance_exhausted`

Therefore, no successful LLM output is claimed for the chatbot or agent.