function friend(friends) {
  return friends.filter(function (name) {
    return name.length === 4;
  });
}

console.log(friend(["Ryan", "Kieran", "Mark"]), "Should be: [\"Ryan\", \"Mark\"]");
console.log(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), "Should be: [\"Ryan\"]");
console.log(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), "Should be: [\"Jimm\", \"Cari\", \"aret\"]");
console.log(friend(["Love", "Your", "Face", "1"]), "Should be: [\"Love\", \"Your\", \"Face\"]");