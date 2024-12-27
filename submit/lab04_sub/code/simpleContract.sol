// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract SimpleContract {
    uint256 public number;
    
    constructor() {
        number = 1;
    }

    function set(uint256 x) public {
        number = x;
    }

    function get() public view returns (uint256) {
        return number;
    }
}

