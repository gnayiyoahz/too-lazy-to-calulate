consSuccess <- function(nCons, pSucc, trialLim, nRep) {
# number of consecutives
# probability of success
# limit -> inf (greater for higher accuracy) 
# number of replications -> inf (greater for higher accuracy)
  
  coin <- c(1,0) # 1 represents a head, 0 represents a tail
  trials <- c(nCons:trialLim)
  cumProb <- c()
  prob <- rep(0, trialLim - nCons + 1)
  
  for (i in trials){
    count <- 0
    for (j in 1:nRep){
      t <- sample(coin, i, replace = TRUE, prob = c(pSucc, 1-pSucc))
      getCons <- grepl(paste(rep(1, nCons), collapse=""), paste(t, collapse=""))
      if (getCons == TRUE) {
        count <- count + 1
      }
    }
    cumProb[i-nCons+1] <- count/nRep
    if (i == nCons){
      prob[1] <- cumProb[1]
    } else {
      prob[i-nCons+1] <- cumProb[i-nCons+1]-cumProb[i-nCons]
    }
  }
  
  plot(trials, prob, type = "l", ylim = c(0,1), col = "blue")
  lines(trials, cumProb, type = "l", ylim = c(0,1), col = "red")
  expect <- sum(trials*prob) 
  expect
}