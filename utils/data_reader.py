import os
import pandas as pd

class QuestionSet: 
    
    def __init__(self, question_group_id, question_group_df):

        self.group_id = question_group_id
        
        match_label, set_label, questions = self.parse_df(question_group_df)
        
        self.match_label = match_label
        self.set_label = set_label
        self.questions = questions
        
    
    def parse_df(self, question_group_df):
        
        sample_row = question_group_df.iloc[0]

        questions = {
            row._14: { # this is the 14th column which is the q number in the set ('#')
                'clue': row.clue,
                'solution': row.solution,
                'right': row.right,                      # no idea what this is
                'wrong': row.wrong,                      # no idea what this is
                'right_team': row.right_team,            # no idea what this is
                'right_team_label': row.right_team_label,
                'wrong_team': row.wrong_team,            # no idea what this is
                'wrong_team_label': row.wrong_team_label,
            }
            for row in question_group_df.itertuples()
        }
        
        return sample_row['match_label'], sample_row['set_label'], questions
    
    def get_qa_tuples(self):
        
        return [
            (question['clue'], question['solution'])
            for question in self.questions.values()
        ]

class QuestionHandler:
    
    def __init__(self, directory):
        
        self.questionsets = self.read_from_directory(directory)
    
    def read_from_directory(self, directory):
        
        questionsets = {}
        
        for filename in os.listdir(directory):
            
            question_df = pd.read_csv(os.path.join(directory, filename))
            
            for question_group_id, question_group_df in question_df.groupby('set'):

                # some of the groups from the show have fewer than 4 questions, so exclude them
                if len(question_group_df) >= 4:
                    
                    questionsets[int(question_group_id)] = QuestionSet(question_group_id, question_group_df)
                
        return questionsets
    
    def __str__(self) -> str:
        
        return f'QuestionHandler with {len(self.questionsets)} questionsets.'
    
    def __len__(self):
        return len(self.questionsets)
    
    def __getitem__(self, key):
        return self.questionsets[key]

    def get_id_set(self):
        
        return set(self.questionsets.keys())