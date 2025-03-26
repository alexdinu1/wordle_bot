# **Wordle Solver**  
### *Created by Alex Dinu*  

## 🔹 Overview  
This is an intelligent agent that solves the game **Wordle** based on user input.  

- The agent minimizes the probability of a word being all gray (`⬜⬜⬜⬜⬜`) to determine the best starting word.  
- It continuously refines its strategy to suggest the most optimal next word.  
- While not yet fully optimal, it is actively updated with improvements and optimizations.  

## 🔹 How It Works  
1. The agent suggests an initial word based on probability calculations.  
2. The user provides feedback using a string that represents Wordle’s color-coded response:  
   - **G** (Green) → Correct letter in the correct position.  
   - **Y** (Yellow) → Correct letter in the wrong position.  
   - **B** (Black/Gray) → Incorrect letter.  
3. The agent processes the feedback and suggests the next best guess.  

## 🔹 Example Gameplay  

### **Example 1**  
#### **Agent's Suggested Word:**  
`clods`
#### **User's Input (Wordle Feedback):**  
`gggyb`
#### **Agent' next Suggested Word (Actual Solution):**  
`cloud`


## 🔹 Notes  
- The solver is not guaranteed to find the correct answer in the minimum number of steps but improves over time.  
- Further optimizations are in progress to enhance accuracy and efficiency.  
