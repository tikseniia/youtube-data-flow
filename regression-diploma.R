library("dplyr")
library("RJSONIO")

model <- rjson::fromJSON(file = "model1.txt")
model <- as.data.frame(model)

d <- data.frame(1:140080)

num <- 1
start <- FALSE
for (i in model) {
  if (num == 122832) {
    start = TRUE
  }
  if (start) {
    d$ad[num] <- i$ad
    d$authorEB[num] <- i$authorEB
    d$authorLE[num] <- i$authorLE
    d$authorWC[num] <- i$authorWC
    d$authorPath[num] <- i$authorPath
    d$authorSubs[num] <- i$authorSubs
    d$authorPG[num] <- i$authorPG
    d$channelViews[num] <- i$channelViews
    d$channelVideo[num] <- i$channelVideo
    d$channelSubs[num] <- i$channelSubs
    d$wc[num] <- i$wc
    d$le[num] <- i$le
    d$eb[num] <- i$eb
    d$shortest[num] <- i$shortest
    d$pagerank[num] <- i$pagerank
    d$wcMatch[num] <- i$wcMatch
    d$leMatch[num] <- i$leMatch
    d$ebMatch[num] <- i$ebMatch
    d$authorViews[num] <- i$authorViews
    d$authorVideo[num] <- i$authorVideo
    d$comment[num] <- i$comment
    d$lendesc[num] <- i$lendesc
    d$http[num] <- i$http
    d$lentitle[num] <- i$lentitle
    d$uppercase[num] <- i$uppercase
    d$like[num] <- i$like
    d$dislike[num] <- i$dislike
    d$view[num] <- i$views
    d$preview[num] <- i$perview
  }
  
  num <- num + 1
}

num <- 1
for (i in model) {
  d$status[num] <- i$status
  d$statusCat[num] <- i$statusCat
  d$authorPG[num] <- unname(i$authorPG)
  d$pagerank[num] <- unname(i$pagerank)
  
  num <- num + 1
}

d$authorSubs <- as.numeric(d$authorSubs)
d$channelViews <- as.numeric(d$channelViews)
d$channelVideo <- as.numeric(d$channelVideo)
d$channelSubs <- as.numeric(d$channelSubs)
d$shortest <- as.numeric(d$shortest)
d$authorViews <- as.numeric(d$authorViews)
d$authorVideo <- as.numeric(d$authorVideo)
d$comment <- as.numeric(d$comment)
d$like <- as.numeric(d$like)
d$dislike <- as.numeric(d$dislike)
d$authorPG <- as.numeric(d$authorPG)
d$pagerank <- as.numeric(d$pagerank)

set.seed(74)
size <- nrow(d)*0.6
d_test <- d[-sample(nrow(d), size), ]
d_test <- select(d_test, -X1.140080, -pagerank, -authorEB, -authorWC, -authorLE, -wc, -le, -eb)
d_train <- d[sample(nrow(d), size), ]
d_train <- select(d_train, -X1.140080, -pagerank, -authorEB, -authorWC, -authorLE, -wc, -le, -eb)
d_all <- select(d, -X1.140080, -pagerank, -authorEB, -authorWC, -authorLE, -wc, -le, -eb)

## LR
linearMod <- lm(status ~ .-statusCat, data=d_train)
summary(linearMod)

linearModCat <- lm(statusCat ~ .-status, data=d_train)
summary(linearModCat)

## RANDOM FOREST
require(randomForest)
rf=randomForest(statusCat ~ .-status, data = d_train)

############

size <- nrow(d_prune)*0.6
d_test <- d_prune[-sample(nrow(d_prune), size), ]
d_train <- d_prune[sample(nrow(d_prune), size), ]

## LR
linearMod <- lm(status ~ .-statusCat, data=d_train)
summary(linearMod)

linearModCat <- lm(statusCat ~ .-status, data=d_train)
summary(linearModCat)

library(ggplot2)
lmpredict <- predict(linearMod, d_test)
ggplot()+geom_point((aes(x=d_test$status, y=lmpredict))) + 
  geom_abline(color="red") +
  xlab("Real value") +
  ylab("Predicted value")

## RANDOM FOREST
require(randomForest)
rf=randomForest(status ~ .-statusCat, data = d_train, type=)
rf
pred <- predict(rf, d_test)
ggplot()+geom_point((aes(x=d_test$status, y=pred))) + 
  geom_abline(color="blue") +
  xlab("Real value") +
  ylab("Predicted value")

## DECISION TREE
library(rpart)
d_train$statusCat <- as.character(d_train$status)
tree <- rpart(status ~ .-statusCat, data=d_train, method="class")
plot(tree)
text(tree)
rsq.rpart(tree)
ptree<- prune(tree, cp=tree$cptable[which.min(tree$cptable[,"xerror"]),"CP"])
plot(ptree)
text(ptree)
rsq.rpart(ptree)

## FEATURE SELECTION
library(mlbench)
library(caret)
# load the data
data(d)
# calculate correlation matrix
d_train <- select(d_train, -preview)
correlationMatrix <- cor(d_train[,1:22])
# summarize the correlation matrix
print(correlationMatrix)
# find attributes that are highly corrected (ideally >0.75)
highlyCorrelated <- findCorrelation(correlationMatrix, cutoff=0.5)
# print indexes of highly correlated attributes
print(highlyCorrelated)

# define the control using a random forest selection function
control <- rfeControl(functions=lmFuncs, method="cv", number=10)
# run the RFE algorithm
results <- rfe(d_train[,1:20], d_train[,22], sizes=c(1:20), rfeControl=control)
# summarize the results
print(results)
# list the chosen features
predictors(results)
# plot the results
plot(results, type=c("g", "o"))

## SVM
library(e1071)
d_train$statusCat <- as.numeric(d_train$statusCat)
model_svm <- svm(statusCat ~ authorPG+authorPath+authorVideo+ad+authorSubs+wcMatch+ebMatch+authorViews+shortest+leMatch+comment+channelSubs+channelVideo+channelViews+dislike, d_train)
pred <- predict(model_svm, d_test)
ggplot()+geom_point((aes(x=d_test$statusCat, y=pred))) + 
  geom_abline(color="blue") +
  xlab("Real value") +
  ylab("Predicted value")

rmse <- function(error)
{
  sqrt(mean(error^2))
}
error <- model_svm$residuals  # same as data$Y - predictedY
predictionRMSE <- rmse(error)
predictionRMSE

svm_linear <- svm(status ~ authorPG+authorPath+authorVideo+ad+authorSubs+wcMatch+ebMatch+authorViews+shortest+leMatch+comment+channelSubs+channelVideo+channelViews+dislike, d_train, kernel="linear")
pred <- predict(svm_linear, d_test)
ggplot()+geom_point((aes(x=d_test$status, y=pred))) + 
  geom_abline(color="blue") +
  xlab("Real value") +
  ylab("Predicted value")
error <- svm_linear$residuals  # same as data$Y - predictedY
predictionRMSE <- rmse(error)
predictionRMSE

d_train$statusCat <- as.factor(d_train$statusCat)
d_test$statusCat <- as.factor(d_test$statusCat)
svm_radial <- svm(statusCat ~ authorPG+authorPath+authorVideo+ad+authorSubs+wcMatch+ebMatch+authorViews+shortest+leMatch+comment+channelSubs+channelVideo+channelViews+dislike, d_train, kernel="radial")
pred <- predict(svm_radial, d_test)
ggplot()+geom_point((aes(x=d_test$statusCat, y=pred))) + 
  geom_abline(color="blue") +
  xlab("Real value") +
  ylab("Predicted value")
error <- svm_radial$residuals  # same as data$Y - predictedY
predictionRMSE <- rmse(error)
predictionRMSE
confusionMatrix(pred, d_train$statusCat)

svm_pol <- svm(status ~ authorPG+authorPath+authorVideo+ad+authorSubs+wcMatch+ebMatch+authorViews+shortest+leMatch+comment+channelSubs+channelVideo+channelViews+dislike, d_train, kernel="polynomial")
pred <- predict(svm_pol, d_test)
ggplot()+geom_point((aes(x=d_test$status, y=pred))) + 
  geom_abline(color="blue") +
  xlab("Real value") +
  ylab("Predicted value")
error <- svm_pol$residuals  # same as data$Y - predictedY
predictionRMSE <- rmse(error)
predictionRMSE

svm_syg <- svm(status ~ authorPG+authorPath+authorVideo+ad+authorSubs+wcMatch+ebMatch+authorViews+shortest+leMatch+comment+channelSubs+channelVideo+channelViews+dislike, d_train, kernel="sigmoid")
pred <- predict(svm_syg, d_test)
ggplot()+geom_point((aes(x=d_test$status, y=pred))) + 
  geom_abline(color="blue") +
  xlab("Real value") +
  ylab("Predicted value")
error <- svm_syg$residuals  # same as data$Y - predictedY
predictionRMSE <- rmse(error)
predictionRMSE

vm_radial.coef_

'ad', 'authorEB', 'authorLE', 'authorWC', 'authorPath', 'authorSubs', 'authorPG', 'channelViews', 'channelVideo', 'channelSubs',
'wc', 'le', 'eb', 'shortest', 'pagerank', 'wcMatch', 'leMatch', 'ebMatch', 'authorPath', 'authorViews',
'authorVideo', 'comment', 'lendesc', 'http', 'lentitle', 'uppercase', 'like', 'dislike', 'view', 'perview'
))
