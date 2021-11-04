//SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

/**
 * Request testnet LINK and ETH here: https://faucets.chain.link/
 * Find information on LINK Token Contracts and get the latest ETH and LINK faucets here: https://docs.chain.link/docs/link-token-contracts/
 */

/**
 * @notice DO NOT USE THIS CODE IN PRODUCTION. This is an example contract.
 */
contract BytesConsumer is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // variable bytes returned in a single oracle response
    bytes public data;
    uint256 public numberOfBytes;
    uint256 public numberOfTimesFulfillmentCalled;

    constructor(
        address link,
        address oracle
    ) {
        setChainlinkToken(link);
        setChainlinkOracle(oracle);
    }

    function requestBytes(
        bytes32 _specId,
        uint256 _payment
    )
    public
    {
        Chainlink.Request memory req = buildChainlinkRequest(
            _specId,
            address(this),
            this.fulfillBytes.selector
        );
        requestOracleData(req, _payment);
    }

    event RequestBytesFulfilled(
        bytes32 indexed requestId,
        bytes indexed data
    );

    function fulfillBytes(
        bytes32 _requestId,
        bytes memory _data
    )
    public
    recordChainlinkFulfillment(_requestId)
    {
        data = _data;
        numberOfBytes = _data.length;
        numberOfTimesFulfillmentCalled++;
        emit RequestBytesFulfilled(_requestId, _data);
    }
}
