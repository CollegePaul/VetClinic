// Pet food calculator
const KCAL_PER_GRAM = 3.6; 
const ACTIVITY = {low: 0.9, normal: 1.0, high: 1.2};

function lifeStageFactor(ageYears) {
    if (ageYears < 1) return 2.5; //puppy or kitten
    if (ageYears < 8) return 1.6; //adult
    return 1.2; //senior
} 

function dailyNeeds(weightKG, ageYears, activity) {
    const restNeed = 70 * Math.pow(weightKG, 0.75); //resting energy need
    const kcal = restNeed * lifeStageFactor(ageYears) * ACTIVITY[activity]
    return {
        kcal: Math.round(kcal),
        grams: Math.round(kcal / KCAL_PER_GRAM)
    };
}

// Get the info from the page
const form = document.getElementById("calc-form");
const weightBox = document.getElementById("weight");
const ageBox = document.getElementById("age");
const activityBox = document.getElementById("activity");
const resultsBox = document.getElementById("result");

form.addEventListener("submit", function (event) {
    event.preventDefault(); //no page reload
    const kg = parseFloat(weightBox.value)
    const age = parseFloat(ageBox.value)
    // console.log(kg)
    // console.log(age)
    
    const needs = dailyNeeds(kg,age, activityBox.value)
    console.log(needs)
})