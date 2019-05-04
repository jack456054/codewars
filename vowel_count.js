function getCount(str) {
  // Regular expression
  return (str.match(/[aeiou]/ig) || []).length;

  //   // Old version
  //   var vowelsCount = 0;
  //   var target = ['a', 'e', 'i', 'o', 'u']
  //   // for(var char=0; char<=str.length; char++){
  //   for (var index in str) {
  //     for (var targetIndex in target) {
  //       if (str[index] == target[targetIndex]) {
  //         vowelsCount += 1;
  //         break;
  //       }
  //     }
  //   }
  //   return vowelsCount;
}

console.log(getCount('asdasdasd'))
console.log(getCount("abracadabra"))