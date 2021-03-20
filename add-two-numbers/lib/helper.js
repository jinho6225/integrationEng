module.exports = exports = function helper(linkedList) {
    console.log(linkedList, 'here')
    let result = []
    if (linkedList.next === null) {
        result.push(String(linkedList.val))
        return Number(result.reverse().join(''))
    } else {
        while (linkedList !== null) {
            result.push(String(linkedList.val))
            linkedList = linkedList.next
        }
        return Number(result.reverse().join(''))
    }
}
