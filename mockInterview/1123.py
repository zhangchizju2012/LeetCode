def num_of_paths_to_dest(n):
  #pass # your code goes here
  dp = [[1] * n for _ in xrange(n)]
  # dp[i][j] 
  # i == j: dp[i][j] = dp[i-1][j]
  # i > j: dp[i][j] = dp[i-1][j] + dp[i][j-1]
  # dp[n-1][n-1]
  for i in xrange(1,n):
    for j in xrange(i,n):
      if i == j:
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
  return dp[n-1][n-1]