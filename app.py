from modules.mfg_tool import tool

if __name__ == '__main__':
    step1 = tool('step1', 3)

    load_parts = ['barcode1', 'barcode2', 'barcode3', 'barcode4', 'barcode5']
    for parts in load_parts:
        check = step1.check_available_slot()
        print(check)
        if step1.check_available_slot():
            step1.load_part(parts)
    
    
    step1.list_loaded_parts()