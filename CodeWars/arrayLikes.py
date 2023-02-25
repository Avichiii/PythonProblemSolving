class Likes():

    def likes(self):
        try:
            how_many_likes = int(input('How many <: '))
            n = how_many_likes
            lis_ = []
            i = 0
            while i<=n:
                input_ = input('array names <: ')
                lis_.append(input_)
                i += 1

            return self.new_likes(lis_)
        except Exception as e:
            print(f'There was an error, {e}')


    
    def new_likes(self, list_of_names):
        
        try:
            len_list_of_names = len(list_of_names)
            
            if len(list_of_names) == 0:
                print('No one like this')
            elif len(list_of_names) == 1:
                print(f'{list_of_names[0]} likes the post')
            elif len(list_of_names) == 2:
                print(f'{list_of_names[0]}, {list_of_names[1]} likes the post.')
            elif len_list_of_names == 3:
                print(f'{list_of_names[0]}, {list_of_names[1]} and {list_of_names[2]} like this')
            elif len_list_of_names > 2:
                print(f'{list_of_names[0]}, {list_of_names[1]} and {len_list_of_names - 2} others like the post.')
        except Exception as e:
            print(f'Error: --> {e}')

if __name__ == '__main__':
    like = Likes()
    like.likes()