

class FieldSelect {

    constructor(_id, _modal_parent=null) {
        this.id = '#' + _id

        if (_modal_parent) {
            this.container = $(this.id).select2({
                theme: "bootstrap",
                dropdownParent: $('#' + _modal_parent)
            })
        } else {
            this.container = $(this.id).select2({
                theme: "bootstrap"
            })
        }
    }

    disable() {
        this.container.prop('disabled', 'disabled');
    }

    enable() {
        this.container.removeAttr('disabled');
    }

    delete_Options() {
        this.container.children('option:not(:first)').remove().trigger('change');
    }

    get_Value() {
        return this.container.val()
    }

    get_Text() {
        var option = this.container.find(':selected');
        return option[0].label
    }

    clear() {
        this.container.val(null).trigger('change')
    }

    fill(_data) {
        _data.forEach(element => {
            var new_option = new Option(element.text, element.id, false, false)
            this.container.append(new_option).trigger('change')
        });
    }
}


export default FieldSelect
