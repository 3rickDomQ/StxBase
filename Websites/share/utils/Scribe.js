
class Scribe {

    static is_Empty(_value) {
        if (
            _value == null ||
            typeof _value == 'undefined' ||
            _value == ""
        ) {
            return true
        } else {
            return false
        }
    }
}


export default Scribe
