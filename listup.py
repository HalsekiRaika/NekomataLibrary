import os;
import json;

def main():
    print("list up")
    check_dir = []
    for config_dir in os.listdir():
        if os.path.isdir(config_dir): 
            if config_dir != ".git":
                check_dir.append(config_dir)

    count = 0
    for configs in check_dir:
        for config_entry in os.scandir(f'./{configs}'):
            if config_entry.name.endswith('.json'):
                count += 1
                with open(f'./{configs}/{config_entry.name}', encoding='utf-8_sig') as open_entry:
                    read_entry = json.load(open_entry)
                    id = read_entry['id']
                    name = read_entry['name']
                    localized_name = read_entry['localized_name']
                    channels = read_entry['channels']
                    print(f'({str(count).rjust(3)}): {id} ', end='')

                    if len(channels) < 1:
                        id = channels[0]['id']
                        print(f'{id} {name.ljust(30)} {localized_name}')
                    else:
                        id = channels[0]['id']
                        print(f'{id} {name.ljust(30)} {localized_name}')
                        for channel in channels[1:]:
                            id = channel['id']
                            print(f'{id.rjust(48)}')
                            

if __name__ == '__main__':
    main()