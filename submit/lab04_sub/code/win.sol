// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

contract Token {
    event SendFlag();
    mapping(address => uint256) balances;
    uint256 public totalSupply;

    constructor() public {}

    function init() public {
        require(balances[msg.sender] == 0);
        balances[msg.sender] += 20;
    }

    function transfer(address _to, uint256 _value) public returns (bool) {
        require(balances[msg.sender] - _value >= 0);
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        return true;
    }

    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner];
    }

    function win() public {
        require(balances[msg.sender] > 20);
        emit SendFlag();
    }
}

