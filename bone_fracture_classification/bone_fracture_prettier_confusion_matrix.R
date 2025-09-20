rm(list = ls())

#install.packages('cvms')
#nstall.packages('ggimage')
#install.packages('rsvg')
library(cvms)
library(plyr)

# Create targets and predictions data frame

results_positive <- read.csv('C:\\Users\\Jo\\Documents\\nitin_chatgpt_project\\bone_fracture_project\\bone_fracture_results\\bone_fracture_frac_4.csv')
results_negative <- read.csv('C:\\Users\\Jo\\Documents\\nitin_chatgpt_project\\bone_fracture_project\\bone_fracture_results\\bone_fracture_nofrac_4.csv')

truth_positive <- rep("A", 500)
truth_negative <- rep("B", 500)

results_positive$truth <- truth_positive
results_negative$truth <- truth_negative

results_total <- rbind.fill(results_positive, results_negative)
results_total[results_total == ""] = NA
results_total <- na.omit(results_total)

data <- data.frame(
  "target" = results_total$truth,
  "prediction" = results_total$result,
  stringsAsFactors = FALSE
)

# Evaluate predictions and create confusion matrix
eval <- evaluate(
  data = data,
  target_col = "target",
  prediction_cols = "prediction",
  type = "binomial"
)

eval

par(mfrow=c(1, 2))
  
# Plot confusion matrix
# Either supply confusion matrix tibble directly
plot_confusion_matrix(eval[["Confusion Matrix"]][[1]])

# Or plot first confusion matrix in evaluate() output
plot_confusion_matrix(eval)
