# CAPM_model

The Capital Asset Pricing Model (CAPM) describes the relationship between the expected return of assets and the systematic risk of the market.
CAPM indicates that the expected return of an asset is equal to the risk-free return plus a risk premium.  The assumption of CAPM is that investors are rational and want to maximize return and reduce risk as much as possible. The goal of CAPM is thus to calculate what return an investor can expect to make for a given risk premium over the risk-free rate.

RISK-FREE-RATE
CAPM also assumes there exists a risk-free asset rf with zero standard deviation. An example of a risk-free asset include Treasury Bills as they're backed by the U.S. government.

MARKET RETURN
The market return is denoted as rm and includes all securities in the market. A good representation of the U.S. market portfolio is the S&P 500, which is a market capitalization-weighted index of the 500 largest U.S. publicly traded companies.

BETA
Beta is a measure of a stock's volatility in relation to the overall market, for example the S&P 500. In other words, Beta represents the slope of the regression line, which is the market return vs. the individual stocks return.Beta is used in the CAPM to describe the relationship between systematic risk, or market risk, and the expected return of an asset. By definition, we say that the overall market has a beta of 1.0 and individual stocks are ranked by how volatile they are relative to the market.
>If the Beta of an individual stock = 1.0, this means its price is perfectly correlated with the market
>If Beta < 1.0, which is referred to as 'defensive', this indicates the security is theoretically less volatile than the market
>If Beta > 1.0, or 'aggressive', this indicates the assets price is more volatile than the market

CAPM Formula
Mathematically, we can define CAPM formula as follows:
ri = rf + βi(rm−rf)
where:
ri = is the expected return of a security
rf = is the risk free rate
βi= is the beta of the security relative to the market
rm − rf is the risk premium

EXAMPLE OF CAPM
Below is an example of the CAPM formula for Apple stock, where we'll make the following (made up) assumptions:
The risk-free rate r1 is 0%
The market portfolio return rm is 12.4%
The beta of Apple βiis 1.11
With these assumptions, we can calculate the CAPM of Apple as:
Expected return = 0% + 1.11(12.4% - 0%) = 13.7%
This formula suggests that an investor should expect a return of 13.7% in order to compensate for the additional risk they're taking.

SUMMARY: Capital Asset Pricing Model with Python
we reviewed how to calculate the Capital Asset Pricing Model (CAPM) with Python. We first defined several key variables that we need for the CAPM formula including the risk-free rate of return, the market return, and beta.We then looked at how to calculate the daily returns for each stock, calculate the beta of an individual stock, and apply the CAPM formula. Finally, we looked at how to use the CAPM formula for an entire portfolio of stocks.
