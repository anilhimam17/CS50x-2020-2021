#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        //printf("The least number of votes was: %i\n", min);

        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}


// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            preferences[voter][rank] = i;
            return true;
        }
    }
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    for (int i = 0; i < voter_count; i++)
    {
        int pref_number = 0;
        int vote_val = preferences[i][pref_number];

        if (candidates[vote_val].eliminated == false)
        {
            candidates[vote_val].votes += 1;
        }

        else
        {
            bool run = true;
            while (run)
            {
                pref_number += 1;
                vote_val = preferences[i][pref_number];

                if (pref_number >= candidate_count)
                {
                    run = false;
                }

                if (candidates[vote_val].eliminated == false)
                {
                    candidates[vote_val].votes += 1;
                    run = false;
                }
            }
        }

    }

    /*for (int i = 0; i < candidate_count; i++){
        printf("The votes acquired by: %s is %i\n", candidates[i].name, candidates[i].votes);
    }*/
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    int majority_votes = ceil(voter_count / 2);

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes > majority_votes)
        {
            printf("%s\n", candidates[i].name);
            return true;
        }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    int least_votes = candidates[0].votes;

    for (int i = 1; i < candidate_count; i++)
    {
        if (candidates[i].votes < least_votes && candidates[i].eliminated == false)
        {
            least_votes = candidates[i].votes;
        }
    }
    return least_votes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    bool tie_val = false;
    int tie_count = 0;
    int no_of_left = 0;

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == false)
        {
            no_of_left += 1;
        }
    }

    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min && candidates[i].eliminated == false)
        {
            tie_count += 1;
        }
    }

    if (tie_count > 1)
    {
        if (tie_count < no_of_left)
        {
            tie_val = false;
        }

        else if (tie_count == no_of_left)
        {
            tie_val = true;
        }
    }

    else
    {
        tie_val = false;
    }
    return tie_val;
}

// Eliminate the candidate (or candidiates) in last place
void eliminate(int min)
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }
    return;
}
