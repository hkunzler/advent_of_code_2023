const fs = require('fs');
const input = fs.readFileSync('./day_one_input_data.txt', 'utf-8');
const arrValues = input.split('\n');

const numberMappings = {
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5five',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine'
};

const getInt = (str) => str.split('').filter(char => !!Number(char))

const getCalibrationValueSum = (arr) => {
    return arr.reduce((acc, str) => {
        const num = getInt(str);
        const firstNum = num[0] || 0
        const lastNum = num[num.length - 1] || 0;
        acc.push(firstNum + lastNum);
        return acc;
    }, []).reduce((acc, num) => acc + parseInt(num), 0);
};

const getCalibrationValueSumWithStringNumbers = (arr) =>
    getCalibrationValueSum(arr.map(str =>
        Object.keys(numberMappings).reduce((acc, num) =>
            acc.replace(new RegExp(num, 'g'), numberMappings[num]), str)
    ));

console.log('The answer when only accounting for numbers in the string: ',getCalibrationValueSum(arrValues));
console.log('The answer when accounting for numbers in the string and spelled out numbers: ', getCalibrationValueSumWithStringNumbers(arrValues));