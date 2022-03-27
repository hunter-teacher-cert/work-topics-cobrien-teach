Code for javascript function is below:

      // finish training function for homework
      train(inputs, desired){
        // store result of feed forward here
        let guess = this.feedForward(inputs)

        // error is difference between desired result and guess
        let error = desired - guess

        // adjust all weights by adding learning rate times error times inputs
        // weight1 + learningRate*error*input1
        // -> do same for all weights
        for (let i = 0; i < this.weights.length; i++){
          this.weights[i] += this.learningRate*error*inputs[i]
        }
      }
