#include <iostream>
#include <vector>
#include <string>
#include <utility>

int main() {
    // Sample sentence with missing tags ("??" and "???")
    std::vector<std::pair<std::string, std::string>> taggedSentence = {
        {"The", "DT"},
        {"planet", "NN"},
        {"Jupiter", "NNP"},
        {"and", "CC"},
        {"its", "??"},  // Missing tag (should be "PRP$" or "PPS")
        {"moons", "NNS"},
        {"are", "VBP"},
        {"in", "IN"},
        {"effect", "???"},  // Missing tag (should be "NN")
        {"a", "DT"},
        {"minisolar", "JJ"},
        {"system", "NN"},
        {",", ","},
        {"and", "CC"},
        {"Jupiter", "NNP"},
        {"itself", "PRP"},
        {"is", "VBZ"},
        {"often", "RB"},
        {"called", "VBN"},
        {"a", "DT"},
        {"star", "NN"},
        {"that", "IN"},
        {"never", "RB"},
        {"caught", "??"},  // Missing tag (should be "VBD")
        {"fire", "NN"},
        {".", "."}
    };

    // Rule structure
    struct TagRule {
        std::string prevTag;  // Previous tag (or "" if none)
        std::string nextTag;  // Next tag (or "" if none)
        std::string resultTag;
    };

    // Rules for missing tags
    std::vector<TagRule> rules = {
        // Two-letter missing tags ("??")
        {"PRP", "", "PRP$"},  // "its" → "PRP$"
        {"VBN", "NN", "VBD"}, // "caught" → "VBD" (past tense)
        {"DT", "", "JJ"},     // Fallback for adjectives
        {"", "", "NN"},      // Default fallback for nouns

        // Three-letter missing tags ("???")
        {"IN", "DT", "NN"},  // "effect" → "NN"
        {"VBP", "NN", "NNP"},
        {"IN", "VBN", "PRP$"}
    };

    // Fill in missing tags
    for (size_t i = 0; i < taggedSentence.size(); ++i) {
        if (taggedSentence[i].second == "??" || taggedSentence[i].second == "???") {
            for (const auto& rule : rules) {
                bool prevMatch = (rule.prevTag.empty() || 
                                (i > 0 && taggedSentence[i-1].second == rule.prevTag));
                bool nextMatch = (rule.nextTag.empty() || 
                                (i < taggedSentence.size() - 1 && 
                                 taggedSentence[i+1].second == rule.nextTag));

                if (prevMatch && nextMatch) {
                    taggedSentence[i].second = rule.resultTag;
                    break;
                }
            }
        }
    }

    // Print the tagged sentence
    for (const auto& token : taggedSentence) {
        std::cout << token.first << "/" << token.second << " ";
    }
    std::cout << std::endl;

    return 0;
}