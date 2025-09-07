# Flex-vs-Power-Play-Calculator

## Overview

The idea of this script is in relation to popular Pick'Em sports betting apps such as Prizepicks, Underdog, and Dabble. For these websites, a bettor will be placing parlays with multiple legs, usually between 2 and 6. However, it is often hard to immediately see what win percentage is necessary for a bettor to break even or even profit on these sites, and many may not realize that the breakeven percentage for each prop is very different across lineups and different apps. This script allows a user to input their number of legs, type of lineup, and payouts, and to see which lineup will give them the best chance at profiting. 

## Functionality

The user is first asked how many props their lineup will contain, and then whether it will be a power play (all legs must hit with the reward of a higher payout) or a flex play (the user can make less money if one or two legs miss, with the downside of a lower payout). Then they are asked for the payout, with the script asking for multiple payouts in the case of a flex play. The script then calculates the breakeven percentage that will be needed on each individual prop for the user to breakeven, given a large enough sample size for variance to even out. 

Breakeven percentage for the user can be calculated a few different ways, although it is not an exact science. One method, in the case of +EV betting, is to use the odds from known, sharp sites such as DraftKings or Fanduel to estimate expecetd win percentages (note that a no vig calculator must be used in this case). The second method is using historical data and backtesting when the legs are from an originated line, specifically from a user's model or own research. This method will most likely be less accurate, therefore this script is more geared towards an EV bettor. 
