#!/usr/bin/env python3
"""
Complete validation script for ShellRosetta enhancements
"""

import subprocess
import sys
import os
from pathlib import Path

def run_test_script(script_path):
    """Run a test script and return success status"""
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, timeout=60)
        
        print(f"Output from {script_path}:")
        print(result.stdout)
        
        if result.stderr:
            print(f"Errors from {script_path}:")
            print(result.stderr)
        
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"❌ {script_path} timed out")
        return False
    except Exception as e:
        print(f"❌ Failed to run {script_path}: {e}")
        return False

def main():
    print("🚀 ShellRosetta Complete Validation Suite")
    print("=" * 60)
    
    test_scripts = [
        "tests/test_imports.py",
        "tests/test_basic_functionality.py", 
        "tests/test_security_complete.py",
        "tests/test_performance_complete.py",
        # Skip API test in automated suite due to server requirements
    ]
    
    results = []
    
    for script in test_scripts:
        if Path(script).exists():
            print(f"\n🧪 Running {script}...")
            print("-" * 40)
            success = run_test_script(script)
            results.append((script, success))
            
            if success:
                print(f"✅ {script} passed")
            else:
                print(f"❌ {script} failed")
        else:
            print(f"⚠️  {script} not found, creating...")
            results.append((script, False))
    
    print("\n" + "=" * 60)
    print("📊 VALIDATION SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for script, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {script}")
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 ALL VALIDATIONS PASSED!")
        print("Your ShellRosetta enhancement is ready for production!")
    else:
        print(f"\n⚠️  {total - passed} validation(s) failed")
        print("Please review the output above and fix any issues.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)