# Day 2 Assessment
## Reasoning and Acting: Direct Prompting vs Chain-of-Thought vs ReAct

## 1. Scenario

The selected scenario is:

"Should I carry an umbrella today in Coimbatore?"

This scenario was selected because it requires current weather information as well as reasoning about whether an umbrella is necessary.

---

## 2. Direct Prompting

Direct prompting asks the language model to answer the question directly without using external tools.

In this experiment, the model was asked whether an umbrella was needed based only on its existing knowledge.

The limitation is that the model does not have access to the current weather information through the prompt.

---

## 3. Chain-of-Thought

Chain-of-Thought prompting was used to encourage the model to analyze the problem before providing its final answer.

The model recognized that it did not have access to real-time weather information and therefore could not reliably determine the current weather.

This demonstrates that reasoning alone cannot provide information that is unavailable to the model.

---

## 4. ReAct Agent

The ReAct approach combines reasoning with actions.

The agent first determined that current weather information was required. It then called the weather tool and received the following observation:

Temperature: 31.4°C
Precipitation: 0.0
Rain: 0.0

The agent then used the tool result to produce its final response.

The workflow was:

Question → Thought → Action → Observation → Final Answer

---

## 5. Comparison

| Basis | Direct Prompting | Chain-of-Thought | ReAct |
|---|---|---|---|
| Reasoning | Direct answer | Multi-step reasoning | Reasoning + action |
| External tools | No | No | Yes |
| Current information | Limited | Limited | Can retrieve through tools |
| Multi-step problems | Basic | Better for reasoning | Useful when tools are required |
| Transparency | Final answer | Reasoning summary | Tool action and observation visible |
| Complexity | Low | Medium | Higher |
| Tool interaction | None | None | Yes |

---

## 6. Self-Consistency Experiment

The same reasoning question was executed five times using a non-zero temperature.

Question:

"A student has an exam tomorrow. They have 3 hours available tonight. They need to study DSA, SQL, and aptitude. What should they study first and why?"

### Results

| Run | Overall Order | Time Allocation |
|---|---|---|
| Run 1 | DSA → SQL → Aptitude | 90 / 45 / 45 min |
| Run 2 | DSA → SQL → Aptitude | 45 / 60 / 75 min |
| Run 3 | DSA → SQL → Aptitude | 90 / 45 / 30 + 15 min buffer |
| Run 4 | DSA → SQL → Aptitude | 75 / 45 / 30 min |
| Run 5 | DSA → SQL → Aptitude | 90 / 45 / 45 min |

### Observation

All five runs selected the same overall order:

DSA → SQL → Aptitude

However, the exact time allocation differed between runs.

This shows that the model's high-level reasoning was consistent while some details of the recommendation varied.

---

## 7. Suitability Analysis

### Direct Prompting

Direct prompting is suitable for simple questions that do not require external information or complex reasoning.

### Chain-of-Thought

Chain-of-Thought is useful when a problem requires multiple reasoning steps. However, reasoning cannot replace missing external information.

### ReAct

ReAct is useful when the task requires both reasoning and interaction with external tools.

In this assessment, the weather tool allowed the agent to obtain current weather information before producing its answer.

---

## 8. Key Findings

1. Direct prompting provides the simplest interaction.
2. Chain-of-Thought improves structured reasoning but does not provide external information.
3. ReAct combines reasoning with tool usage.
4. The ReAct agent successfully retrieved weather information before answering.
5. The self-consistency experiment showed stable high-level recommendations with variation in detailed time allocation.

---

## 9. Conclusion

The experiment demonstrates that the three approaches have different capabilities.

Direct prompting is the simplest approach.

Chain-of-Thought is useful for problems requiring additional reasoning.

ReAct extends the process by allowing the model to interact with external tools. This makes it useful for tasks where current or external information is required.
