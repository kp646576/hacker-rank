import Foundation;

/*
    1. Traverse string to get and store unique characters
    2. If len(unique char) > 2, select different combinations of 2 and loop through
        2a. Stop if adjacent characaters detected
    3. Repeat 2 for all combinations
    
    ** Notes:
        - Don't have to necessarily delete, just skip if not the designated character
        - Keep max variable on hand
        - 
*/

func checker(t: String, c1: Character, c2: Character) -> Int {
    // Loop through t and look for c1 and c2
    var prev: Character? = nil
    var len: Int = 0
    for c in t.characters {
        // Character is one of the two we're looking at
        if c == c1 || c == c2 {
            
            // If it's the same as the previous it's a duplicate so return
            if prev != nil && c == prev {
                return 0
            } else {
                // Set up for next iteration
                prev = c
                len += 1
            }
        }
    }
    
    // Return length of valid two characters given c1 and c2
    return len
}

func twoCharacters(str: String) -> Int {
    var curMaxLen: Int = 0
    var maxLen: Int = 0
    var uniqueCharacters: [Character] = []
    
    // Find number of unique characters in str
    for c in str.characters {
        if !uniqueCharacters.contains(c) {
            uniqueCharacters.append(c)
        }
    }
    
    let startIndex = uniqueCharacters.startIndex
    let uniqueLength = uniqueCharacters.count
    
    for i in 0...uniqueLength-1 {
        let c1 = uniqueCharacters.index(startIndex, offsetBy: i)
        if i < uniqueLength-1 {
            for j in i+1...uniqueLength-1 {
                let c2 = uniqueCharacters.index(startIndex, offsetBy: j)
                
                // Check combination
                curMaxLen = checker(t: str, c1: uniqueCharacters[c1], c2: uniqueCharacters[c2])
                
                // Set the maxLen accordingly
                maxLen = curMaxLen > maxLen ? curMaxLen : maxLen
            }
        }
    }
    return maxLen
}

let strLen = readLine()!
let str = readLine()!
print(twoCharacters(str: str))
